window.onload = function () {

    function createBarChart(containerId, data, yAxisLabel, chartTitle, valueKey) {
        if (Array.isArray(data)) {
            data.sort((a, b) => a[valueKey] - b[valueKey]);
        } else {
            console.error("Data is not an array.");
            return;
        }

        const width = 1000;
        const height = 500;
        const margin = { top: 30, right: 20, bottom: 80, left: 60 };

        const svg = d3.select(`#${containerId}`)
            .append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        const xScale = d3.scaleBand()
            .domain(data.map(d => d.location))
            .range([0, width])
            .padding(0.1);

        const yScale = d3.scaleLinear()
            .domain([0, d3.max(data, d => d[valueKey])])
            .range([height, 0]);

        svg.append('g')
            .attr('transform', `translate(0, ${height})`)
            .call(d3.axisBottom(xScale))
            .selectAll("text")
            .attr("transform", "rotate(-45)")
            .style("text-anchor", "end");

        svg.append('g')
            .call(d3.axisLeft(yScale));

        const rainbowColorScale = d3.scaleSequential(d3.interpolateRainbow)
            .domain([0, data.length - 1]);

        svg.selectAll('rect')
            .data(data)
            .enter()
            .append('rect')
            .attr('x', d => xScale(d.location))
            .attr('y', d => (yScale(d[valueKey]) || 0) - 10)
            .attr('width', xScale.bandwidth())
            .attr('height', d => height - (yScale(d[valueKey]) || 0))
            .attr('fill', (d, i) => rainbowColorScale(i))
            .attr('stroke', 'black')
            .attr('stroke-width', 1)
            .on('mouseover', function (data) {
                d3.select(this)
                    .attr('stroke', 'black')
                    .attr('stroke-width', 2);

                const [x, y] = d3.mouse(this);

                const chartContainer = document.getElementById('chart-container');
                const containerRect = chartContainer.getBoundingClientRect();

                const tooltip = d3.select('#info');
                tooltip.html(`
                    <strong>${data.location}</strong><br>
                    Population: ${data.population}<br>
                    Vaccination Rate: ${data.vaccination_rate}%<br>
                    Measles Cases: ${data.cases}<br>
                    Cases per 100,000: ${data.cases_100000}
                `)
                    .style('left', `${x + containerRect.left}px`)
                    .style('top', `${y + containerRect.top}px`);
            })
            .on('mouseout', function () {
                d3.select(this)
                    .attr('stroke', 'black')
                    .attr('stroke-width', 1);

                const tooltip = d3.select('#info');
                tooltip.html('');
            });

        svg.selectAll('.bar-label')
            .data(data)
            .enter()
            .append('text')
            .text(d => d[valueKey])
            .attr('class', 'bar-label')
            .attr('x', d => xScale(d.location) + xScale.bandwidth() / 2)
            .attr('y', d => (yScale(d[valueKey]) || 0) + 5)
            .attr('text-anchor', 'middle')
            .attr('fill', 'black');

        svg.append('text')
            .attr('x', width / 2)
            .attr('y', 0 - (margin.top / 2))
            .attr('text-anchor', 'middle')
            .style('font-size', '16px')
            .style('text-decoration', 'underline')
            .text(chartTitle);
    }

    function createScatterplot(containerId, data) {
        const width = 1200;
        const height = 500;
        const margin = { top: 30, right: 20, bottom: 80, left: 60 };

        const svg = d3.select(`#${containerId}`)
            .append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        const xScale = d3.scaleLinear()
            .domain([d3.min(data, d => d.population), d3.max(data, d => d.population)])
            .range([0, width]);

        const yScale = d3.scaleLinear()
            .domain([0, d3.max(data, d => d.cases)])
            .range([height, 0]);

        const radiusScale = d3.scaleSqrt()
            .domain([0, d3.max(data, d => d.population)])
            .range([2, 20]);

        const rainbowColorScale = d3.scaleSequential(d3.interpolateRainbow)
            .domain([0, data.length - 1]);

        const simulation = d3.forceSimulation(data)
            .force('x', d3.forceX(d => xScale(d.population)).strength(0.1))
            .force('y', d3.forceY(d => yScale(d.cases)).strength(0.1))
            .force('collide', d3.forceCollide(d => radiusScale(d.population) + 2).iterations(4));

        const circles = svg.selectAll('circle')
            .data(data)
            .enter()
            .append('circle')
            .attr('r', d => radiusScale(d.population / 100  * d.cases)) // Adjusted size
            .attr('fill', (d, i) => rainbowColorScale(i))
            .on('mouseover', function (d) {
                const [x, y] = d3.mouse(this);

                const chartContainer = document.getElementById('chart-container');
                const containerRect = chartContainer.getBoundingClientRect();

                const tooltip = d3.select('#info1');
                tooltip.html(`
                    <strong>${d.location}</strong><br>
                    Population: ${d.population}<br>
                    Measles Cases: ${d.cases}
                `)
                    .style('left', `${x + containerRect.left}px`)
                    .style('top', `${y + containerRect.top}px`);

                d3.select(this)
                    .attr('stroke', 'black')
                    .attr('stroke-width', 2);
            })
            .on('mouseout', function () {
                d3.select(this)
                    .attr('stroke', 'none');

                const tooltip = d3.select('#info1');
                tooltip.html('');
            });

        simulation.on('tick', () => {
            circles.attr('cx', d => d.x)
                .attr('cy', d => d.y);
        });

        svg.append('g')
            .attr('transform', `translate(0, ${height})`)
            .call(d3.axisBottom(xScale))
            .selectAll("text")
            .attr("transform", "rotate(-45)")
            .style("text-anchor", "end");

        // hide the axis
        // svg.selectAll('g.axis path')
        // .style('display', 'none');

        svg.append('g')
            .call(d3.axisLeft(yScale));

        svg.append('text')
            .attr('x', width / 2)
            .attr('y', height + margin.top + 20)
            .attr('text-anchor', 'middle')
            .text('Population');

        svg.append('text')
            .attr('transform', 'rotate(-90)')
            .attr('x', 0 - height / 2)
            .attr('y', 0 - margin.left)
            .attr('dy', '1em')
            .attr('text-anchor', 'middle')
            .text('Measles Cases');

        svg.append('text')
            .attr('x', width / 2)
            .attr('y', 0 - (margin.top / 2))
            .attr('text-anchor', 'middle')
            .style('font-size', '16px')
            .style('text-decoration', 'underline')
            .text('Measles Cases in Cities');
    }

    function updateChart() {
        const chartSelection = document.getElementById('chart-selection');
        const selectedChart = chartSelection.value;
        const chartContainer = document.getElementById('chart-container');
        chartContainer.style.display = selectedChart ? 'block' : 'none';

        d3.select('#chart-container').selectAll('*').remove();

        const baseURL = window.location.hostname === 'localhost' ? 'http://localhost:8000' : '';

        const fetchMeaslesData = fetch(`${baseURL}/measlesdata1`)
            .then(response => response.json());

        const fetchCitiesData1 = fetch(`${baseURL}/citiesupto200000`)
            .then(response => response.json());

        const fetchCitiesData2 = fetch(`${baseURL}/citiesmorethan200000`)
            .then(response => response.json());

        const fetchCitiesData3 = fetch(`${baseURL}/citiesmorethan500000`)
            .then(response => response.json());

        const fetchCitiesData4 = fetch(`${baseURL}/citiesmorethan1000000`)
            .then(response => response.json());

        Promise.all([fetchMeaslesData, fetchCitiesData1, fetchCitiesData2, fetchCitiesData3, fetchCitiesData4])
            .then(([measlesData, citiesData1, citiesData2, citiesData3, citiesData4]) => {
                if (Array.isArray(measlesData) && Array.isArray(citiesData1) && Array.isArray(citiesData2) && Array.isArray(citiesData3) && Array.isArray(citiesData4)) {
                    if (selectedChart === 'measles') {
                        createBarChart('chart-container', measlesData, 'Cases per 100,000', 'Measles Cases per 100,000', 'cases_100000');
                    } else if (selectedChart === 'vaccination') {
                        createBarChart('chart-container', measlesData, 'Vaccination Rate', 'Vaccination Rate by Bundesland', 'vaccination_rate');
                    } else if (selectedChart === 'cities_population1') {
                        createScatterplot('chart-container', citiesData1);
                    } else if (selectedChart === 'cities_population2') {
                        createScatterplot('chart-container', citiesData2);
                    } else if (selectedChart === 'cities_population3') {
                        createScatterplot('chart-container', citiesData3);
                    } else if (selectedChart === 'cities_population4') {
                        createScatterplot('chart-container', citiesData4);
                    }
                } else {
                    console.error('Invalid data format:', measlesData, citiesData1, citiesData2, citiesData3, citiesData4);
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    updateChart();

    const chartSelection = document.getElementById('chart-selection');
    if (chartSelection) {
        chartSelection.onchange = function () {
            updateChart();
        };
    } else {
        console.error("Element with ID 'chart-selection' not found.");
    }
};
