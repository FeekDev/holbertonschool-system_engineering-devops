#this puppet kill a process name

exec {'killmenow':
command  => 'pkill -f killmenow',
provider => 'shell',
}
