import sys
import os
import shutil
import win32api
import win32con
import winioctlcon


def getFileName(name):
    filename = name.split("\\")[-1]
    return filename


def copyFile(filename, fulll_dir_name, targertfile):
    targertfileUnDo = targertfile + '\\' + filename
    targertfileName = targertfileUnDo.replace(r"\\", "\\")
    shutil.copyfile(fulll_dir_name, targertfileName)
    print(targertfile)
    return targertfileName


def copyDir(filename, fulll_dir_name, targertfile):
    targertfileUnDo = targertfile + '\\' + filename
    targertfileName = targertfileUnDo.replace(r"\\", "\\")
    if (os.path.exists(targertfileName)):
        shutil.rmtree(targertfileName)
    shutil.copytree(fulll_dir_name, targertfileName)
    print(targertfile)
    return targertfileName


def openFile(targetfilename, targetfile):
    if (targetfilename.find("ppt") != -1):
        win32api.ShellExecute(0, 'open', 'POWERPNT.EXE', targetfilename, '', 1)
    elif (targetfilename.find("doc") != -1):
        win32api.ShellExecute(0, 'open', 'WINWORD.EXE', targetfilename, '', 1)
    elif (targetfilename.find("pdf") != -1):
        win32api.ShellExecute(0, 'open', 'Acrobat.exe', targetfilename, '', 1)
    else:
        win32api.ShellExecute(0, 'open', 'explorer.exe', targetfile, '', 1)


if __name__ == '__main__':
    full_dir_name = sys.argv[1]
    if (full_dir_name.find('.') != -1):
        print('选中为文件')
        filename = getFileName(full_dir_name)
        targetfile = 'C:\\Users\高一·（1）班\Desktop\生物'
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('复制后将自动退出')
        targetfilename = copyFile(filename, full_dir_name, targetfile)
        openFile(targetfilename, targetfile)
    else:
        print('选中为文件夹')
        filename = getFileName(full_dir_name)
        targetfile = 'C:\\Users\高一·（1）班\Desktop\生物'
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('文件复制中，请稍等')
        print('复制后将自动退出')
        targetfilename = copyDir(filename, full_dir_name, targetfile)
        openFile(targetfilename, targetfilename)
    win32api.MessageBox(0, "操作完成，单击确定退出", "操作结果", win32con.MB_RIGHT)
    # win32api.DeviceIoControl("D", winioctlcon.IOCTL_STORAGE_EJECT_MEDIA, NULL, 0, NULL, 0, NULL)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
