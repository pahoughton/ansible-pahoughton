# 2018-10-13 (cc) <paul4hough@gmail.com>
#

# 2018-10-10 (cc) <paul4hough@gmail.com>
#
# y = rake recurses down (. .. ../..:)

$runstart = Time.now

at_exit {
  runtime = Time.at(Time.now - $runstart).utc.strftime("%H:%M:%S.%3N")
  puts "run time: #{runtime}"
}

task :default do
  sh 'rake --tasks'
  exit 1
end

task :galaxy do
  sh "ansible-galaxy install -r require-roles.yml -p roles"
end

task :lint do
  sh "yamllint ."
end

task :ansible_syntax do |task, args|
  sh "ansible-playbook --syntax-check --list-tasks site.yml -i cbed,"
end

task :provision do |task, args|
  sh "vagrant provision cbed"
end

task :test, [:backend] do | task, args|
  Dir.chdir('testinfra') do
    sh "py.test -v"
  end
end
