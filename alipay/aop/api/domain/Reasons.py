#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Reasons(object):

    def __init__(self):
        self._problem_pic = None
        self._remark = None
        self._risk_name = None

    @property
    def problem_pic(self):
        return self._problem_pic

    @problem_pic.setter
    def problem_pic(self, value):
        if isinstance(value, list):
            self._problem_pic = list()
            for i in value:
                self._problem_pic.append(i)
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def risk_name(self):
        return self._risk_name

    @risk_name.setter
    def risk_name(self, value):
        self._risk_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.problem_pic:
            if isinstance(self.problem_pic, list):
                for i in range(0, len(self.problem_pic)):
                    element = self.problem_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.problem_pic[i] = element.to_alipay_dict()
            if hasattr(self.problem_pic, 'to_alipay_dict'):
                params['problem_pic'] = self.problem_pic.to_alipay_dict()
            else:
                params['problem_pic'] = self.problem_pic
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.risk_name:
            if hasattr(self.risk_name, 'to_alipay_dict'):
                params['risk_name'] = self.risk_name.to_alipay_dict()
            else:
                params['risk_name'] = self.risk_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Reasons()
        if 'problem_pic' in d:
            o.problem_pic = d['problem_pic']
        if 'remark' in d:
            o.remark = d['remark']
        if 'risk_name' in d:
            o.risk_name = d['risk_name']
        return o


