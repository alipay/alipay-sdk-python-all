#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TargetInfo import TargetInfo


class AlipayMerchantTradecomplainBatchqueryModel(object):

    def __init__(self):
        self._begin_time = None
        self._end_time = None
        self._page_num = None
        self._page_size = None
        self._status = None
        self._target_infos = None

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_infos(self):
        return self._target_infos

    @target_infos.setter
    def target_infos(self, value):
        if isinstance(value, list):
            self._target_infos = list()
            for i in value:
                if isinstance(i, TargetInfo):
                    self._target_infos.append(i)
                else:
                    self._target_infos.append(TargetInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.begin_time:
            if hasattr(self.begin_time, 'to_alipay_dict'):
                params['begin_time'] = self.begin_time.to_alipay_dict()
            else:
                params['begin_time'] = self.begin_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_infos:
            if isinstance(self.target_infos, list):
                for i in range(0, len(self.target_infos)):
                    element = self.target_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_infos[i] = element.to_alipay_dict()
            if hasattr(self.target_infos, 'to_alipay_dict'):
                params['target_infos'] = self.target_infos.to_alipay_dict()
            else:
                params['target_infos'] = self.target_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantTradecomplainBatchqueryModel()
        if 'begin_time' in d:
            o.begin_time = d['begin_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        if 'target_infos' in d:
            o.target_infos = d['target_infos']
        return o


