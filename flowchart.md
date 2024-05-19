<section><p>
basic flow mermaid code:
graph TD
    Start --> GetSchedule
    GetSchedule --> CreateTaskList
    CreateTaskList --> StartTasks
    StartTask --> CheckTimer
    CheckTimer --5 Minutes Left--> WarningNotification
    CheckTimer --Task Complete--> AlarmNotification
    AlarmNotification --> NextTask[Is there another task?]
    NextTask --Yes--> StartTask
    NextTask --No--> End 
    </p> </section>
<section><p>
Flow:


[![](https://mermaid.ink/img/pako:eNptkcFqwzAMhl_F-Nwed8lhY7RjDNpcEihj3kHEamMS28FWoKP03Sfb28hofZJ-fb8syxfZeY2ykqcAUy_arXKCT0MQSKzXj-IVqel61POIpbQQMrAJCIQtxGFnIhXmv5ax3DEpiwtSWnr02A2tsRh-_H85lx_E3riZMIodHinhBwjOuFPtyRxNB2S8u-PL3TfeTiMSJtvzCMHemm7kPFKN5zzfx1sU1GNAAc6nQBCrT5_F-0ux5R3jnXcugNqn-ovTQjm5kjykBaN59ZeEKsnNLSpZcaghDEoqd2UOZvLNl-tkRWHGlZwnzbvdGuAfs0W8fgOviJZ0?type=png)](https://mermaid.live/edit#pako:eNptkcFqwzAMhl_F-Nwed8lhY7RjDNpcEihj3kHEamMS28FWoKP03Sfb28hofZJ-fb8syxfZeY2ykqcAUy_arXKCT0MQSKzXj-IVqel61POIpbQQMrAJCIQtxGFnIhXmv5ax3DEpiwtSWnr02A2tsRh-_H85lx_E3riZMIodHinhBwjOuFPtyRxNB2S8u-PL3TfeTiMSJtvzCMHemm7kPFKN5zzfx1sU1GNAAc6nQBCrT5_F-0ux5R3jnXcugNqn-ovTQjm5kjykBaN59ZeEKsnNLSpZcaghDEoqd2UOZvLNl-tkRWHGlZwnzbvdGuAfs0W8fgOviJZ0)
</p> </section>

![alt text](image-1.png)