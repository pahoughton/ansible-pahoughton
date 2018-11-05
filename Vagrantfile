# 2018-10-13 (cc) <paul4hough@gmail.com>
#

Vagrant.configure("2") do |config|
  config.vm.box_check_update = false

  config.vm.define 'vcbed' do |bcfg|
    bcfg.vm.box = "ubuntu/xenial64"
    bcfg.vm.hostname = 'vcbed'
    bcfg.vm.network    'private_network', ip: '10.1.1.10'
    # bcfg.vm.network "forwarded_port", guest: 3000, host: 13000
    # bcfg.vm.network "forwarded_port", guest: 8086, host: 18086
    bcfg.vm.provider 'virtualbox' do |vb|
      vb.name      = 'vcbed'
      vb.cpus      = 2
      vb.memory    = 2048
      vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
      vb.customize ['modifyvm', :id, '--natdnspassdomain1', 'on']
      vb.customize ['modifyvm', :id, '--usb', 'off']
    end
    bcfg.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/cbed.yml"
      ansible.extra_vars = {
        ansible_python_interpreter:"/usr/bin/python3"
      }
    end
  end
end
