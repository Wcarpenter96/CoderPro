function canFinish(numCourses, prerequisites) {
    const visited = new Set();
    const visiting = new Set();
    const prereqs = []
    for (let i = 0; i < numCourses; i++) {
        prereqs.push([])
    }

    for (let [prereq, course] of prerequisites) {
        prereqs[course].push(prereq);
    }

    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) {
            return false;
        }
    }
    return true;

    function dfs(course) {
        if (visited.has(course)) return true;
        if (visiting.has(course)) return false;

        visiting.add(course);
        for (let prereq of prereqs[course]) {
            if (!dfs(prereq)) {
                return false;
            }
        }
        visiting.delete(course);
        visited.add(course);
        return true;
    }
}


console.log(canFinish(4, [[0, 1], [1, 2], [2, 3], [0, 3], [1, 3] ]))