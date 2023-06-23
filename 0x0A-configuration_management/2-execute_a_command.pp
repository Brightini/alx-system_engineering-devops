# This manifest kills a process

exec {'pkill':
    command => ['pkill', killmenow]
}
