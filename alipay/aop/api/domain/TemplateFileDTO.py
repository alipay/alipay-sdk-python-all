#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateFileDTO(object):

    def __init__(self):
        self._can_present = None
        self._can_share = None
        self._format_version = None
        self._serial_number = None

    @property
    def can_present(self):
        return self._can_present

    @can_present.setter
    def can_present(self, value):
        self._can_present = value
    @property
    def can_share(self):
        return self._can_share

    @can_share.setter
    def can_share(self, value):
        self._can_share = value
    @property
    def format_version(self):
        return self._format_version

    @format_version.setter
    def format_version(self, value):
        self._format_version = value
    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_present:
            if hasattr(self.can_present, 'to_alipay_dict'):
                params['can_present'] = self.can_present.to_alipay_dict()
            else:
                params['can_present'] = self.can_present
        if self.can_share:
            if hasattr(self.can_share, 'to_alipay_dict'):
                params['can_share'] = self.can_share.to_alipay_dict()
            else:
                params['can_share'] = self.can_share
        if self.format_version:
            if hasattr(self.format_version, 'to_alipay_dict'):
                params['format_version'] = self.format_version.to_alipay_dict()
            else:
                params['format_version'] = self.format_version
        if self.serial_number:
            if hasattr(self.serial_number, 'to_alipay_dict'):
                params['serial_number'] = self.serial_number.to_alipay_dict()
            else:
                params['serial_number'] = self.serial_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateFileDTO()
        if 'can_present' in d:
            o.can_present = d['can_present']
        if 'can_share' in d:
            o.can_share = d['can_share']
        if 'format_version' in d:
            o.format_version = d['format_version']
        if 'serial_number' in d:
            o.serial_number = d['serial_number']
        return o


