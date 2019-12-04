import sys

class VirtualMachine:
    def __init__(self, name, ram=1, cpu=1.3, hdd=100, os="debian"):
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        self.os = os
        self.status = 0
        self.proc = []

    def status_view(self):
        if self.status == 0:
            return 'Stopped'

        elif self.status == 1:
            return 'Running'

        elif self.status == 2:
            return 'Suspended'

    def stop(self):
        self.status = 0
        self.proc = []

    def start(self):
        self.status = 1

    def suspend(self):
        self.status = 2

    def reboot(self):
        self.stop
        self.start

    def run(self, pid, ram, cpu, hdd):
        processes = {
            'pid' : pid,
            'ram' : ram,
            'cpu' : cpu,
            'hdd' : hdd
        }
        self.proc.append(processes)
        print(f'''Ejecutando proceso con PID {pid}...''')

    def ram_usage(self):
        ram = 0
        for processes in self.proc:
            ram += processes['ram']
        usedram = ram * 100 / self.ram
        return usedram

    def hdd_usage(self):
        hdd = 0
        for processes in self.proc:
            hdd += processes['hdd']
        usedhdd = hdd * 100 / self.hdd
        return usedhdd

    def cpu_usage(self):
        cpu = 0
        for processes in self.proc:
            cpu += processes['cpu']
        usedcpu = cpu * 100 / self.cpu
        return usedcpu

    def __str__(self):
        return f'''
{self.os} <{self.name}> [{self.status_view()}]
{self.ram_usage():.2f}% RAM used | {self.cpu_usage():.2f}% CPU used | {self.hdd_usage():.2f}% HDD used\n'''

if __name__ == '__main__':
    vm1 = VirtualMachine('Minas Tirith', 8, 2.3, 380, 'Ubuntu')
    print(vm1)
    vm1.start()
    print(vm1)
    vm1.run(1,1.7,0.3,20)
    vm1.run(4,4,0.9,100)
    vm1.run(7,0.4,1.1,250)
    print(vm1)



    vm2 = VirtualMachine('Rohan', 6, 1.9, 250, 'Debian')
    print(vm2)
    vm2.start()
    print(vm2)
    vm2.run(2,0.6,0.7,50)
    vm2.run(5,2.1,0.2,75)
    vm2.run(8,2.5,0.4,30)
    print(vm2)



    vm3 = VirtualMachine('Rivendel', 16, 3, 100, 'OpenSuse')
    print(vm3)
    vm3.start()
    print(vm3)
    vm3.run(3,2,1,25)
    vm3.run(6,0.3,0.5,12)
    vm3.run(9,1.4,0.8,65)
    print(vm3)
