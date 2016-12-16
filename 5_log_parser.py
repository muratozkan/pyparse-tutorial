from pyparsing import Word, nums, oneOf, Suppress, restOfLine, alphas, alphanums, Group, ZeroOrMore

# Parses Spring log lines (logs are taken from ENBD project)

log_sample = '''
2016-08-01 11:27:21.047  WARN 22458 --- [http-bio-8080-exec-24] c.m.enbd.core.AbstractEnbdController     : POST /goal/daily: User haven't defined a goal yet
2016-08-01 17:54:47.908  INFO 22458 --- [http-bio-8080-exec-27] com.monitise.enbd.core.RequestFilter     : Handling request, /version, POST
2016-08-01 17:54:47.909  INFO 22458 --- [http-bio-8080-exec-30] com.monitise.enbd.core.RequestFilter     : Handling request, /features, POST
2016-08-01 17:54:47.914  DEBUG 22458 --- [http-bio-8080-exec-30] c.m.enbd.core.AbstractEnbdController     : getting IOS features
2016-08-01 17:54:47.924  INFO 22458 --- [http-bio-8080-exec-27] c.m.enbd.core.AbstractEnbdController     : checking version for device code: 1 and device OS: 10.0 and version: 1.0.3'''

date = Word(nums + '-')
time = Word(nums + ':.')
level = oneOf(['INFO', 'WARN', 'DEBUG'])
pid = Word(nums)
thread = Suppress('[') + Word(alphanums + '-') + Suppress(']')
source = Word(alphas + '.')
message = restOfLine

log_line = Group(date + time + level + pid + Suppress('---') + thread + source + Suppress(':') + message)
logs = ZeroOrMore(log_line)

print(logs.parseString(log_sample))

# So, if you design log strings that can be parsed, you can actually parse them
