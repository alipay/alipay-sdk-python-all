#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderChangeInfoExtIstd(object):

    def __init__(self):
        self._work_pic_link = None

    @property
    def work_pic_link(self):
        return self._work_pic_link

    @work_pic_link.setter
    def work_pic_link(self, value):
        if isinstance(value, list):
            self._work_pic_link = list()
            for i in value:
                self._work_pic_link.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.work_pic_link:
            if isinstance(self.work_pic_link, list):
                for i in range(0, len(self.work_pic_link)):
                    element = self.work_pic_link[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_pic_link[i] = element.to_alipay_dict()
            if hasattr(self.work_pic_link, 'to_alipay_dict'):
                params['work_pic_link'] = self.work_pic_link.to_alipay_dict()
            else:
                params['work_pic_link'] = self.work_pic_link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderChangeInfoExtIstd()
        if 'work_pic_link' in d:
            o.work_pic_link = d['work_pic_link']
        return o


