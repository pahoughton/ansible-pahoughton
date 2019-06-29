# 2018-10-13 (cc) <paul4hough@gmail.com>
#

Vagrant.configure("2") do |config|
  config.vm.box_check_update = false

  name = 'vrand'
  config.vm.define name do |bcfg|
    bcfg.vm.box = "c7g"
    bcfg.vm.hostname = name
    bcfg.vm.network    'private_network', ip: '10.0.0.10'
    # bcfg.vm.network "forwarded_port", guest: 3000, host: 13000
    # bcfg.vm.network "forwarded_port", guest: 8086, host: 18086
    bcfg.vm.provider 'virtualbox' do |vb|
      vb.name      = name
      vb.cpus      = 2
      vb.memory    = 2048
      vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
      vb.customize ['modifyvm', :id, '--natdnspassdomain1', 'on']
      vb.customize ['modifyvm', :id, '--usb', 'off']
    end
    bcfg.vm.provision "ansible" do |a|
      a.playbook = "ansible/#{name}.yml"
      a.inventory_path = "ansible/inventory"
      # a.extra_vars = {
      #   ansible_python_interpreter:"/usr/bin/python"
      # }
    end
  end
end
