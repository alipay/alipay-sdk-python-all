#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuditLicenseInfo(object):

    def __init__(self):
        self._license_name = None
        self._license_no = None
        self._license_pic_list = None
        self._license_valid_date = None
        self._out_door_pic = None

    @property
    def license_name(self):
        return self._license_name

    @license_name.setter
    def license_name(self, value):
        self._license_name = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def license_pic_list(self):
        return self._license_pic_list

    @license_pic_list.setter
    def license_pic_list(self, value):
        if isinstance(value, list):
            self._license_pic_list = list()
            for i in value:
                self._license_pic_list.append(i)
    @property
    def license_valid_date(self):
        return self._license_valid_date

    @license_valid_date.setter
    def license_valid_date(self, value):
        self._license_valid_date = value
    @property
    def out_door_pic(self):
        return self._out_door_pic

    @out_door_pic.setter
    def out_door_pic(self, value):
        self._out_door_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_name:
            if hasattr(self.license_name, 'to_alipay_dict'):
                params['license_name'] = self.license_name.to_alipay_dict()
            else:
                params['license_name'] = self.license_name
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        if self.license_pic_list:
            if isinstance(self.license_pic_list, list):
                for i in range(0, len(self.license_pic_list)):
                    element = self.license_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.license_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.license_pic_list, 'to_alipay_dict'):
                params['license_pic_list'] = self.license_pic_list.to_alipay_dict()
            else:
                params['license_pic_list'] = self.license_pic_list
        if self.license_valid_date:
            if hasattr(self.license_valid_date, 'to_alipay_dict'):
                params['license_valid_date'] = self.license_valid_date.to_alipay_dict()
            else:
                params['license_valid_date'] = self.license_valid_date
        if self.out_door_pic:
            if hasattr(self.out_door_pic, 'to_alipay_dict'):
                params['out_door_pic'] = self.out_door_pic.to_alipay_dict()
            else:
                params['out_door_pic'] = self.out_door_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuditLicenseInfo()
        if 'license_name' in d:
            o.license_name = d['license_name']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'license_pic_list' in d:
            o.license_pic_list = d['license_pic_list']
        if 'license_valid_date' in d:
            o.license_valid_date = d['license_valid_date']
        if 'out_door_pic' in d:
            o.out_door_pic = d['out_door_pic']
        return o


