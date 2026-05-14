#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InpatientNursingServiceResult(object):

    def __init__(self):
        self._service_summary_photo_url_list = None

    @property
    def service_summary_photo_url_list(self):
        return self._service_summary_photo_url_list

    @service_summary_photo_url_list.setter
    def service_summary_photo_url_list(self, value):
        if isinstance(value, list):
            self._service_summary_photo_url_list = list()
            for i in value:
                self._service_summary_photo_url_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.service_summary_photo_url_list:
            if isinstance(self.service_summary_photo_url_list, list):
                for i in range(0, len(self.service_summary_photo_url_list)):
                    element = self.service_summary_photo_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_summary_photo_url_list[i] = element.to_alipay_dict()
            if hasattr(self.service_summary_photo_url_list, 'to_alipay_dict'):
                params['service_summary_photo_url_list'] = self.service_summary_photo_url_list.to_alipay_dict()
            else:
                params['service_summary_photo_url_list'] = self.service_summary_photo_url_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InpatientNursingServiceResult()
        if 'service_summary_photo_url_list' in d:
            o.service_summary_photo_url_list = d['service_summary_photo_url_list']
        return o


