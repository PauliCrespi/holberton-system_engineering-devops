#task 3

exec { 'pkill':
  command  =>  'pkill -f killmenow',
  provider => 'shell',
}
