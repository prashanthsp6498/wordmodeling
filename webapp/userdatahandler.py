import os
import webapp


user_config = {}
user_config['basedir'] = webapp.module_dir + '/dbfiles'
user_config['userhash'] = ''


def get_user_files(userdir):
    path = os.path.join(user_config['basedir'], userdir)
    return os.listdir(path)


def create_user_directory(dirname):
    directory = os.path.join(user_config['basedir'], dirname)
    os.mkdir(directory)


def create_user_file(userdir, filename):
    path = os.path.join(user_config['basedir'],
                        userdir, filename)
    print(path)
    with open(path, "w") as f:
        pass


def read_user_file(userdir, filename):
    data = ''
    with open(os.path.join(user_config['basedir'], userdir, filename)) as f:
        data = f.read()
    data = data.splitlines()
    return data


def save_to_file(userdir, filename, data):
    with open(os.path.join(user_config['basedir'], userdir, filename), "w") as f:
        f.write(data)
    return "success"
