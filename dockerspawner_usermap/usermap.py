import dockerspawner
import pwd
import grp

from traitlets import Unicode


class DockerUsermapSpawner(dockerspawner.DockerSpawner):

    group_name = Unicode('developer', config=True)
    settings_module = Unicode('drtools.conf.global_settings', config=True)

    def get_env(self):
        env = super(DockerUsermapSpawner, self).get_env()
        user_env = self.get_user_env()
        env.update(user_env)
        return env

    def get_user_env(self):
        user_env = {
            'LOCAL_GROUP_ID': grp.getgrnam(self.group_name).gr_gid,
            'LOCAL_USER_ID': pwd.getpwnam(self.user.name).pw_uid,
            'LOCAL_USER': self.user.name,
            'NOTEBOOK_DIR': '/home/{}'.format(self.user.name),
            'PYTHONPATH': '/home/{}/bin'.format(self.user.name),
            'DRTOOLS_SETTINGS_MODULE': self.settings_module
            }
        return user_env