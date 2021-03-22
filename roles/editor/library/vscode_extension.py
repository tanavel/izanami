#!/usr/bin/python

# Copyright: (c) 2020, tanavel <tanavel1118@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: vscode_extension

short_description: Manage extensions for Visual Studio Code

version_added: "2.9"

description:
    - You can install or uninstall VScode extension
    - This is needed installing Visual Studio Code

options:
    name:
        description:
            - extension name.
        type: str
        required: true
    state:
        description:
            - present or absent.
        type: str
        default: present
        required: false

author:
    - tanavel (@tanavel)
'''

EXAMPLES = '''
- vscode_extension:
    name: vscoss.vscode-ansible

- vscode_extension:
    name: vscoss.vscode-ansible
    state: absent
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
    returned: always
message:
    description: The output message that the test module generates
    type: str
    returned: always
'''

import re
from ansible.module_utils.basic import AnsibleModule

class VScodeExtensionException(Exception):
    def __init__(self, msg):
        self.message = msg

class VScodeExtension():
    def __init__(self, module):
        self.module = module
        self.target_extension = module.params['name']
        self.state = module.params['state']

        self.executable = self.module.get_bin_path(
            'code',
            required=True
        )
        self.extensions = self.get_extensions()

    def run_module(self):

        result = dict(
            changed=False,
        )

        if self.module.check_mode:
            module.exit_json(**result)

        if self.state == 'present':
            result['changed'] = self.install()

        if self.state == 'absent':
            result['changed'] = self.uninstall()

        self.module.exit_json(**result)

    def install(self):
        if self.has_extension():
            return False

        rc, out, err = self.module.run_command([self.executable] + ['--install-extension', self.target_extension])
        if rc == 1:
            raise VScodeExtensionException(err)
        return True

    def uninstall(self):
        if not self.has_extension():
            return False
        rc, out, err = self.module.run_command([self.executable] + ['--uninstall-extension', self.target_extension])
        if rc == 1:
            raise VScodeExtensionException(err)
        return True

    def get_extensions(self):
        rc, out, err = self.module.run_command([self.executable] + ['--list-extensions'])
        if rc == 1:
            raise VScodeExtensionException(err)
        return out.split('\n')

    def has_extension(self):
        for installed_extension in self.extensions:
            m = re.compile(self.target_extension, re.IGNORECASE).match(installed_extension)
            if m != None:
                return True
        return False

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            state=dict(type='str', default='present', choices=['absent', 'present']),
        ),
        supports_check_mode=True
    )
    try:
        vscode_extension = VScodeExtension(module=module)
        vscode_extension.run_module()
    except VScodeExtensionException as e:
        module.fail_json(msg=e.message)

if __name__ == '__main__':
    main()
