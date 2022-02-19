Create Docker Container
---
1. เปิด Docker Desktop
2. เปิด Settings
3. ไม่ใช้ Use Docker Compose V2 และ Appyle & Restart
4. เปิด VSCode ไปที่ Path ที่เก็บ Mayan-EDMS
5. เข้าไปโฟลเดอร์ `docker/` คลิ๊กขวาเปิด Open in Integrated Terminal
6. ใน Terminal พิมพ์ `docker-compose up`
7. เช็คใน Docker Desktop

Install VSCode Extension
---
Remote - Containers: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

Remote into Docker Container
---
1. เปิด Docker เพื่อ Start Container
![](Docs\img\Docker_start.png)
รอเป็นสีเขียวทั้งหมด
![](Docs\img\Docker_after_start.png)

2. เปิด Menu ชื่อ Remote Explorer มน VSCode
![](Docs\img\Remote_Ex.png)

3. เลือก Remote ไปที่ Mayan-app
![](Docs\img\Remote_ex2.png)

4. Open Folder
![](Docs\img\Remote_ex3.png)

5. เปลี่ยนไปยัง Path: `/opt/mayan-edms/lib/python3.7/site-packages/`
![](Docs\img\Remote_ex4.png)

6. 