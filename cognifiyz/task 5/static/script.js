let tasks = [];
const taskTableBody = document.querySelector("#taskTable tbody");
let filterStatus = "All";

// Load tasks
async function loadTasks() {
    const res = await axios.get("/tasks");
    tasks = res.data;
    renderTasks();
}

// Render tasks
function renderTasks() {
    taskTableBody.innerHTML = "";
    tasks.filter(t => filterStatus === "All" || t.status === filterStatus)
         .forEach(task => {
        const tr = document.createElement("tr");
        tr.setAttribute("draggable", true);
        tr.innerHTML = `
            <td>${task.id}</td>
            <td contenteditable="true" onblur="updateTaskField(${task.id}, 'name', this.innerText)">${task.name}</td>
            <td>
                <select class="form-select" onchange="updateTaskField(${task.id}, 'status', this.value)">
                    <option value="Pending" ${task.status==='Pending'?'selected':''}>Pending</option>
                    <option value="Done" ${task.status==='Done'?'selected':''}>Done</option>
                </select>
            </td>
            <td>
                <select class="form-select" onchange="updateTaskField(${task.id}, 'priority', this.value)">
                    <option value="Low" ${task.priority==='Low'?'selected':''}>Low</option>
                    <option value="Medium" ${task.priority==='Medium'?'selected':''}>Medium</option>
                    <option value="High" ${task.priority==='High'?'selected':''}>High</option>
                </select>
            </td>
            <td><input type="date" class="form-control" value="${task.due_date}" onchange="updateTaskField(${task.id}, 'due_date', this.value)"></td>
            <td><button class="btn btn-danger btn-sm" onclick="deleteTask(${task.id})">Delete</button></td>
        `;
        // Drag and drop events
        tr.addEventListener('dragstart', dragStart);
        tr.addEventListener('dragover', dragOver);
        tr.addEventListener('drop', drop);
        taskTableBody.appendChild(tr);
    });
}

// Add task
async function addTask() {
    const name = document.getElementById("taskName").value;
    const status = document.getElementById("taskStatus").value;
    const priority = document.getElementById("taskPriority").value;
    const due_date = document.getElementById("taskDueDate").value;
    if(!name) return alert("Task name required");
    await axios.post("/tasks", {name, status, priority, due_date});
    document.getElementById("taskName").value="";
    document.getElementById("taskDueDate").value="";
    loadTasks();
}

// Update field
async function updateTaskField(id, field, value) {
    const task = tasks.find(t => t.id === id);
    task[field] = value;
    await axios.put(`/tasks/${id}`, task);
    loadTasks();
}

// Delete task
async function deleteTask(id) {
    if(confirm("Delete this task?")) {
        await axios.delete(`/tasks/${id}`);
        loadTasks();
    }
}

// Filter tasks
function filterTasks(status) {
    filterStatus = status;
    renderTasks();
}

// Search tasks
function searchTasks() {
    const term = document.getElementById("searchTask").value.toLowerCase();
    const filtered = tasks.filter(t => t.name.toLowerCase().includes(term));
    taskTableBody.innerHTML = "";
    filtered.forEach(task => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${task.id}</td>
            <td contenteditable="true" onblur="updateTaskField(${task.id}, 'name', this.innerText)">${task.name}</td>
            <td>${task.status}</td>
            <td>${task.priority}</td>
            <td>${task.due_date}</td>
            <td><button class="btn btn-danger btn-sm" onclick="deleteTask(${task.id})">Delete</button></td>
        `;
        taskTableBody.appendChild(tr);
    });
}

// Drag-and-drop
let dragged;
function dragStart(e){ dragged = e.target; }
function dragOver(e){ e.preventDefault(); }
function drop(e){
    e.preventDefault();
    if(e.target.tagName === "TD") e.target = e.target.parentElement;
    taskTableBody.insertBefore(dragged, e.target.nextSibling);
}

loadTasks();
