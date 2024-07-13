#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
import subprocess


def subp_send_cmd(cmd_list: List):
    """执行一个外部命令，并且返回它的执行结果和标准输出内容
    如果发生任何错误，返回执行结果和标准错误信息
    @return: (bool, str): 执行结果和返回字符串
    """
    (ret, cmd_ret_str) = (True, '')
    try:
        cmd_ret_str = subprocess.check_output(
                cmd_list, stderr=subprocess.STDOUT, encoding='utf-8',
                errors='ignore')
    except subprocess.CalledProcessError as sub_err:
        (ret, cmd_ret_str) = (False, sub_err.output)

    return (ret, cmd_ret_str)
