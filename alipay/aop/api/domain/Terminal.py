#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Terminal(object):

    def __init__(self):
        self._mac = None
        self._os = None
        self._os_arch = None
        self._os_version = None
        self._terminal_type = None
        self._terminal_version = None

    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, value):
        self._mac = value
    @property
    def os(self):
        return self._os

    @os.setter
    def os(self, value):
        self._os = value
    @property
    def os_arch(self):
        return self._os_arch

    @os_arch.setter
    def os_arch(self, value):
        self._os_arch = value
    @property
    def os_version(self):
        return self._os_version

    @os_version.setter
    def os_version(self, value):
        self._os_version = value
    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value
    @property
    def terminal_version(self):
        return self._terminal_version

    @terminal_version.setter
    def terminal_version(self, value):
        self._terminal_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.mac:
            if hasattr(self.mac, 'to_alipay_dict'):
                params['mac'] = self.mac.to_alipay_dict()
            else:
                params['mac'] = self.mac
        if self.os:
            if hasattr(self.os, 'to_alipay_dict'):
                params['os'] = self.os.to_alipay_dict()
            else:
                params['os'] = self.os
        if self.os_arch:
            if hasattr(self.os_arch, 'to_alipay_dict'):
                params['os_arch'] = self.os_arch.to_alipay_dict()
            else:
                params['os_arch'] = self.os_arch
        if self.os_version:
            if hasattr(self.os_version, 'to_alipay_dict'):
                params['os_version'] = self.os_version.to_alipay_dict()
            else:
                params['os_version'] = self.os_version
        if self.terminal_type:
            if hasattr(self.terminal_type, 'to_alipay_dict'):
                params['terminal_type'] = self.terminal_type.to_alipay_dict()
            else:
                params['terminal_type'] = self.terminal_type
        if self.terminal_version:
            if hasattr(self.terminal_version, 'to_alipay_dict'):
                params['terminal_version'] = self.terminal_version.to_alipay_dict()
            else:
                params['terminal_version'] = self.terminal_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Terminal()
        if 'mac' in d:
            o.mac = d['mac']
        if 'os' in d:
            o.os = d['os']
        if 'os_arch' in d:
            o.os_arch = d['os_arch']
        if 'os_version' in d:
            o.os_version = d['os_version']
        if 'terminal_type' in d:
            o.terminal_type = d['terminal_type']
        if 'terminal_version' in d:
            o.terminal_version = d['terminal_version']
        return o


