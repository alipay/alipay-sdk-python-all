#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommonTextReq import CommonTextReq


class CreateTextRequest(object):

    def __init__(self):
        self._common_text_list = None
        self._publish_flag = None
        self._work_id = None

    @property
    def common_text_list(self):
        return self._common_text_list

    @common_text_list.setter
    def common_text_list(self, value):
        if isinstance(value, list):
            self._common_text_list = list()
            for i in value:
                if isinstance(i, CommonTextReq):
                    self._common_text_list.append(i)
                else:
                    self._common_text_list.append(CommonTextReq.from_alipay_dict(i))
    @property
    def publish_flag(self):
        return self._publish_flag

    @publish_flag.setter
    def publish_flag(self, value):
        self._publish_flag = value
    @property
    def work_id(self):
        return self._work_id

    @work_id.setter
    def work_id(self, value):
        self._work_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.common_text_list:
            if isinstance(self.common_text_list, list):
                for i in range(0, len(self.common_text_list)):
                    element = self.common_text_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.common_text_list[i] = element.to_alipay_dict()
            if hasattr(self.common_text_list, 'to_alipay_dict'):
                params['common_text_list'] = self.common_text_list.to_alipay_dict()
            else:
                params['common_text_list'] = self.common_text_list
        if self.publish_flag:
            if hasattr(self.publish_flag, 'to_alipay_dict'):
                params['publish_flag'] = self.publish_flag.to_alipay_dict()
            else:
                params['publish_flag'] = self.publish_flag
        if self.work_id:
            if hasattr(self.work_id, 'to_alipay_dict'):
                params['work_id'] = self.work_id.to_alipay_dict()
            else:
                params['work_id'] = self.work_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreateTextRequest()
        if 'common_text_list' in d:
            o.common_text_list = d['common_text_list']
        if 'publish_flag' in d:
            o.publish_flag = d['publish_flag']
        if 'work_id' in d:
            o.work_id = d['work_id']
        return o


