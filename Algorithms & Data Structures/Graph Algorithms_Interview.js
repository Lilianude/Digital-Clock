// Iterative Depth First search
// // using a stack

// const depthFirstPrint = (graph, source) => {
//     const stack = [ source ];

//     while (stack.length > 0){
//         const current = stack.pop();
//         console.log(current);

//         for (let neighbour of graph[current]){
//             stack.push(neighbour);
//         }
//     }
// }; 
// Recursive depth First Search

// const depthFirstPrint = (graph, source) => {
//     console.log(source);
//     for (let neighbour of graph[source]){
//         depthFirstPrint(graph, neighbour)
//     }
// };

//  // ITERATIVE BREADTH FIRST SEARCH
// const breadthFirstPrint = (graph, source) => {
//     const queue = [ source ];
//     while (queue.length > 0){
//         const current  = queue.shift();
//         console.log(current);

//         for (let neighbour of graph[source]){
//             queue.push(neighbour)
//         }
//     }
// };

// const graph = {
//     a: ['b','c'],
//     b: ['d'],
//     c: ['e'],
//     d: ['f'],
//     e: [],
//     f: []
// }

// // depthFirstPrint(graph, 'a');

// breadthFirstPrint(graph,'a');


// HAS PATH RECURSIVE DFS

// const hasPath = (graph, src, dst) => {
//     // bases case
//     if (src === dst) return true;

//     for (let neighbour of graph[src]) {
//         if (hasPath(graph, neighbour, dst) === true) {
//             return true;
//         }
//     }
//     return False
// };

// There is no way to do a BFS recursively, but only iteratively

//ITERATIVE BFS FOR HASPATH

// const hasPath = (graph, src, dst) => {
//     const queue = [src];

//     while(queue.length > 0){
//         const current = queue.shift();
//         if (current == dst) return true;

//         for (let neighbour of graph[current]){
//             queue.push(neighbour);
//         }
//     }
//     return false;

// };

// const graph = {
//     f:['g','i'],
//     g:['h'],
//     h:[],
//     i:['g','k'],
//     j:['i'],
//     k:[]
// };

// hasPath(graph, 'f', 'k');


// // UNDIRECTED PATH QUESTION
// const undirectedPath = (edges, nodeA,nodeB) => {
//     const graph = buildGraph(edges);
//      return hasPath(graph, nodeA, nodeB, new Set());
// };

// const hasPath = (graph,src, dst, visited) => {
//     if (visited.has(src)) return false;
//     if (src === dst) return true;

//     visited.add(src);

//     //else go through the neighbours of the src node find out if haspath is through by calling recursively
//     for (let neighbour of graph[src]){
//         if (hasPath(graph, neighbour,dst, visited) === true) {
//             return true;
//         }
//     }
//     return False
// };



// const buildGraph = (edges) => {
//     const graph = {};

//     for (let edge of edges){
//         const [a,b] = edge; // unpacking the edge
//         if (!(a in graph)) graph[a] = []
//         if (!(b in graph)) graph[b] = []
//         graph[a].push(b); // if a,b as neighbours of themselves
//         graph[b].push(a); // undirected graph, b should point to a as a to b 
//     }

//     return graph;
// };



// const edges = [
//     ['i','j'],
//     ['k','i'],
//     ['m','k'],
//     ['k','l'],
//     ['o','n'],  
//  ];

// undirectedPath(edges,"j","m");

// CONNECTED COMPONENTS COUNT

// const connectedComponentsCount= (graph) => {
//     let count = 0;
//     const visited = new Set();

//     for (let node in graph){
//         console.log(visited);
//         if  (explore(graph, node, visited) === true) {
//             count += 1;
//         }
//     }
//     return count

// };

// const explore = (graph, current, visited) => {
//     if (visited.has(String(current))) return false;
    
//     visited.add(String(current));

//     for (let neighbour of graph[current]){
//         explore(graph,neighbour, visited);
//     }
//     return true;
// };


// connectedComponentsCount ({
//     0: [8,1,5],
//     1:[0],
//     5:[0,8],
//     8:[0,5],
//     2:[3,4],
//     3:[2,4],
//     4:[3,2]
// });

// console.log(connectedComponentsCount());



// LARGEST COMPONENT

// const largestComponent = (graph) => {
//     let longest = 0;
//     const visited = new Set();

//     for ( let node in graph){
//         const size = checkSize( graph, node, visited);
        
//         if (size > longest){
//             return longest = size;
//         }
//     }
//     return longest
// };

// const checkSize = (graph, current , visited) => {
//     if (visited.has(current)) return 0

//     visited.add(current);

//     let size = 1; // reps the current node i am on.
//     for(let neighbour of graph[current]){
//         size += checkSize(graph, neighbour, visited)
//     }
//     return size;
// };

// graph = {
//         0: ['8','1','5'],
//         1:['0'],
//         5:['0','8'],
//         8:['0','5'],
//         2:['3','4'],
//         3:['2','4'],
//         4:['3','2']
// }

// console.log(largestComponent(graph));

// SHORTEST PATH PROBLEM

// const shortestPath = (edges, nodeA, nodeB) => {
//     const graph = buildGraph(edges);
//     const visited = new Set([ nodeA ]); // initialize the set
//     const queue = [ [nodeA, 0] ]; // initialize the queue.

//     while (queue.length > 0) {
//         console.log(queue)
//         const [node, distance] = queue.shift();

//         if (node === nodeB ) return distance;
//         // else traverse through the neighbours to look for shortest path

//         for ( let neighbour of graph[node] ){
//             if (!(visited.has(neighbour))) {
//                 visited.add(neighbour);
//                 queue.push([neighbour, distance + 1]);
//             }
//         }
//     }
//     return -1;
// };

// // Building graph here because we are only given the edges
// const buildGraph = (edges) => {
//     const graph = {};

// //     for(let edge of edges){
//         console.log(graph);
//         const [a,b] = edge; // we are unpacking the edges into its nodes
//         if (!(a in graph)){ // if a node is not in the graph as a key then
//             graph[a] = []; // initialize it here
//         }
//         if (!(b in graph)){
//             graph[b] = [];
//         }
//         graph[a].push(b); // a is a neigbor of b
//         graph[b].push(a); // b is a neighbor of a
//     }
//     return graph;
// };


// edges = [
//     ['w','x'],
//     ['x','y'],
//     ['z','y'],
//     ['z','v'],
//     ['w','v']
// ];


// ISLAND PROBLEM

// const islandCount = (grid) => {
//     const visited = new Set();
//     let count  = 0;
//     for (let r = 0 ; r < grid.length; r += 1){
//         for ( let c = 0; c < grid[0].length; c += 1){
//            if (explore(grid,r,c,visited) === true) {
//                count += 1;
//            }
//         }
//     }
//     return count;
// };

// const explore = (grid,r,c,visited) => {
//     // check if both r and c are in bounds  before checking if current postn is Water
//     const rowInbounds = 0 < r && r < grid.length;
//     const colInbounds = 0 < c && c < grid[0].length;
//     if (!rowInbounds || !colInbounds) return false;

//     if (grid[r][c] == 'W') return false;


//     const pos = r + ',' + c;
//     if (visited.has(pos)) return false;
//     visited.add(pos);

//     // now check the neighbours
//     explore(grid,r - 1,c,visited);
//     explore(grid,r + 1,c,visited);
//     explore(grid,r,c - 1,visited);
//     explore(grid,r,c + 1,visited);

//     return true; 
// };

// const grid = [
//     ['W','L','W','W','W'],
//     ['W','L','W','W','W'],
//     ['W','W','W','L','W'],
//     ['W','W','L','L','W'],
//     ['L','W','W','L','L'],
//     ['L','L','W','W','W'],
// ];

// console.log(islandCount(grid));


// MINUMUM ISLAND COUNT

const minimumIsland = (grid) => {
    const visited = new Set();
    let minSize = Infinity;
    for(let r = 0; r < grid.length; r += 1){
        for(let c = 0; c< grid[0].length; c += 1){
            const size = exploreSize(grid, r,c,visited);
            if (size > 0 && size < minSize){ 
                minSize = size
            }
        }
    }
    return minSize;

};

const exploreSize = (grid, r, c, visited) => {
    
    rowInbounds = r >= 0 && r < grid.length;
    colInbounds = c >= 0 && c < grid[0].length;

    if (!rowInbounds || !colInbounds) return 0;
    if (grid[r][c] === 'W') return 0;

    const pos = r + ',' + c;
    if (visited.has(pos)) return 0;
    visited.add(pos);
    
    let size = 1;
    size += exploreSize(grid, r-1, c,visited);
    size += exploreSize(grid, r+1, c,visited);
    size += exploreSize(grid, r, c-1,visited);
    size += exploreSize(grid, r, c+1,visited);

    return size;
};

const grid = [
    ['W', 'L','W','W','W'],
    ['W', 'L','W','W','W'],
    ['W', 'W','W','L','W'],
    ['W', 'W','L','L','W'],
    ['L', 'W','W','L','L'],
    ['L', 'L','W','W','W'],
];

console.log(minimumIsland(grid));