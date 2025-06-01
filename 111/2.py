import requests
import time

# 这个里面填入videoid,taskid,步长，循环次数，有些任务没有videoid可以随便填一个，具体参数自己抓
tasks = [
    {"video_id": "1891540198139039745", "task_id": "1001", "step": 10, "loops": 500},
    {"video_id": "1891540198139039745", "task_id": "1003", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "1004", "step": 10, "loops": 500},
    {"video_id": "1891540198139039745", "task_id": "1002", "step": 10, "loops": 500},
    {"video_id": "1892882353879687168", "task_id": "2001", "step": 10, "loops": 500},
    {"video_id": "1892882353879687169", "task_id": "3001", "step": 10, "loops": 500},
    {"video_id": "1892882466119262208", "task_id": "4001", "step": 10, "loops": 500},
    {"video_id": "1892882466119262209", "task_id": "5001", "step": 10, "loops": 500},
    {"video_id": "1892882502257385472", "task_id": "6001", "step": 10, "loops": 500},
    {"video_id": "1892882502257385473", "task_id": "7001", "step": 10, "loops": 500},
    {"video_id": "1892882539553136640", "task_id": "8001", "step": 10, "loops": 500},
    {"video_id": "1891540198139039745", "task_id": "1004", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "2001", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "2002", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "2003", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "2004", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "2005", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "3001", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "3002", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "3003", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "3004", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "3005", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "3006", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "3007", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "3008", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "4001", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "4002", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "4003", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "4004", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "4005", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "4006", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "5001", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "5002", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "5003", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "5004", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "5005", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "5006", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "5007", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "6001", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "6002", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "6003", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "6004", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "6005", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "7001", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "7002", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "7003", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "7004", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "8001", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "8002", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "8003", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "8004", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "8005", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "8006", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "8007", "step": 10, "loops": 100},
    {"video_id": "1891540198139039745", "task_id": "9001", "step": 10, "loops": 100},
]

URL = "http://10.106.2.144/ncut/api/s/taskInfo/finishTask"

def load_cookies(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def run_for_cookie(cookie):
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."
    }

    for task in tasks:
        current_duration = 0
        step = task["step"]
        loops = task["loops"]
        task_id = task["task_id"]
        video_id = task["video_id"]

        print(f"\n开始执行任务：task_id={task_id}, video_id={video_id}")

        for i in range(loops):
            data = {
                "currentDuration": current_duration,
                "duration": step,
                "taskId": task_id,
                "videoId": video_id
            }
            try:
                response = requests.post(URL, headers=headers, json=data, timeout=10)
               ### print(f"[{i+1}] 发送中：currentDuration = {current_duration}, 状态码 = {response.status_code}")
            except Exception as e:
                print(f"请求出错：{e}")
                break

            current_duration += step
            #time.sleep(0)

        print("任务完成\n")

if __name__ == "__main__":
    cookies = load_cookies("cookie.txt")
    print(f"共加载 {len(cookies)} 个用户")

    for idx, cookie in enumerate(cookies, start=1):
        print(f"\n======= 开始处理第 {idx} 个用户 =======")
        run_for_cookie(cookie)
        print(f"======= 第 {idx} 个用户完成 =======\n")
