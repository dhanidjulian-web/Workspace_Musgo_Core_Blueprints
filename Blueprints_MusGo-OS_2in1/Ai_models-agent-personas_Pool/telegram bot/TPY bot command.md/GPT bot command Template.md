Berikut template generik yang bisa dijadikan fondasi untuk bot autonomous, scheduler, multi-task manager, assistant agent, workflow engine, brainstorming agent, dan task orchestrator. Semua placeholder bisa diubah/replace sesuai kebutuhan.

##################################################

CONFIGURATION

##################################################

CONFIG = {
"BOT_NAME": "Assistant",
"ADMIN_ID": 123456789,
"MAX_TASKS": 100,
"AUTO_RETRY": True,
"RETRY_LIMIT": 3,
"DEFAULT_DELAY": 60
}

##################################################

PLACEHOLDER VARIABLES

##################################################

USER_ID      = message.from_user.id
USERNAME     = message.from_user.first_name
TEXT         = message.text
TIMESTAMP    = int(time.time())

##################################################

MEMORY

##################################################

def memory_get(key):
return getData(key)

def memory_set(key, value):
saveData(key, value)

def memory_delete(key):
deleteData(key)

##################################################

TASK OBJECT

##################################################

def create_task(
name,
description,
priority="normal",
status="pending",
payload=None
):
return {
"id": str(int(time.time())),
"name": name,
"description": description,
"priority": priority,
"status": status,
"created_at": int(time.time()),
"payload": payload
}

##################################################

TASK QUEUE

##################################################

def add_task(task):

tasks = memory_get("task_queue")

if not tasks:
    tasks = []

tasks.append(task)

memory_set(
    "task_queue",
    tasks
)

def get_tasks():
return memory_get("task_queue")

def clear_tasks():
memory_delete("task_queue")

##################################################

SCHEDULER

##################################################

def schedule_task(
command_name,
delay_seconds
):

runCommandAfter(
    delay_seconds,
    command_name
)

##################################################

AUTONOMOUS EXECUTOR

##################################################

def execute_task(task):

try:

    task["status"] = "running"

    if task["name"] == "research":

        runCommand(
            "research_worker"
        )

    elif task["name"] == "brainstorm":

        runCommand(
            "brainstorm_worker"
        )

    elif task["name"] == "analysis":

        runCommand(
            "analysis_worker"
        )

    elif task["name"] == "report":

        runCommand(
            "report_worker"
        )

    task["status"] = "completed"

except:

    task["status"] = "failed"

##################################################

MULTI TASK PROCESSOR

##################################################

/run_tasks

tasks = get_tasks()

if not tasks:

bot.sendMessage(
    "Queue kosong"
)

else:

completed = 0

for task in tasks:

    execute_task(task)

    completed += 1

bot.sendMessage(
    "Selesai: " +
    str(completed)
)

##################################################

CREATE TASK

##################################################

/task

bot.sendMessage(
"Masukkan nama task"
)

handleNextCommand(
"task_name"
)

task_name

memory_set(
"tmp_task_name_" +
str(USER_ID),
TEXT
)

bot.sendMessage(
"Masukkan deskripsi"
)

handleNextCommand(
"task_description"
)

task_description

name = memory_get(
"tmp_task_name_" +
str(USER_ID)
)

task = create_task(
name=name,
description=TEXT
)

add_task(task)

bot.sendMessage(
"Task ditambahkan"
)

##################################################

BRAINSTORM AGENT

##################################################

brainstorm_worker

topic = memory_get(
"brainstorm_topic"
)

prompt = """
Buat 20 ide kreatif untuk:
""" + str(topic)

kirim ke AI API

proses hasil

##################################################

RESEARCH AGENT

##################################################

research_worker

query = memory_get(
"research_query"
)

HTTP request

search API

save result

##################################################

REPORT GENERATOR

##################################################

report_worker

data = memory_get(
"research_result"
)

report = {
"summary": "",
"insights": [],
"actions": []
}

memory_set(
"latest_report",
report
)

##################################################

RECURSIVE LOOP

##################################################

autonomous_loop

tasks = get_tasks()

if tasks:

for task in tasks:

    if task["status"] == "pending":

        execute_task(task)

runCommandAfter(
CONFIG["DEFAULT_DELAY"],
"autonomous_loop"
)

##################################################

GOAL SYSTEM

##################################################

/goal

memory_set(
"goal_" +
str(USER_ID),
params
)

bot.sendMessage(
"Goal disimpan"
)

##################################################

OBJECTIVE PLANNER

##################################################

planner_worker

goal = memory_get(
"goal_" +
str(USER_ID)
)

plan = {
"goal": goal,
"steps": [
"step_1",
"step_2",
"step_3"
]
}

memory_set(
"active_plan",
plan
)

##################################################

CONTEXT MEMORY

##################################################

def save_context(text):

memory_set(
    "context_" +
    str(USER_ID),
    text
)

def load_context():

return memory_get(
    "context_" +
    str(USER_ID)
)

##################################################

VARIABLE TEMPLATE

##################################################

{{BOT_NAME}}
{{TASK_NAME}}
{{TASK_ID}}
{{GOAL}}
{{OBJECTIVE}}
{{PROMPT}}
{{USER_INPUT}}
{{CONTEXT}}
{{RESULT}}
{{REPORT}}
{{ACTION}}
{{NEXT_STEP}}
{{DEADLINE}}
{{STATUS}}
{{MEMORY_KEY}}
{{API_URL}}
{{API_KEY}}
{{MODEL}}
{{SCHEDULE}}
{{WORKFLOW}}
{{QUEUE}}
{{OUTPUT}}

##################################################

MASTER AUTONOMOUS FLOW

##################################################

Input
↓
Save Context
↓
Analyze
↓
Create Tasks
↓
Prioritize
↓
Execute
↓
Validate
↓
Store Result
↓
Generate Report
↓
Schedule Next Action
↓
Repeat
##################################################Template ini sengaja dibuat generik sehingga Anda cukup mengganti placeholder seperti {{GOAL}}, {{PROMPT}}, {{API_URL}}, {{MODEL}}, {{WORKFLOW}}, dll. untuk membangun berbagai jenis agen: personal assistant, autonomous researcher, scheduler, task manager, content creator, workflow automation, atau multi-agent orchestrator.