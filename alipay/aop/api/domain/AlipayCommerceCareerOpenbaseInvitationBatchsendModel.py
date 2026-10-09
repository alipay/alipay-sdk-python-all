#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CareerOpenBaseInvitationDetail import CareerOpenBaseInvitationDetail


class AlipayCommerceCareerOpenbaseInvitationBatchsendModel(object):

    def __init__(self):
        self._batch_details = None
        self._out_batch_no = None

    @property
    def batch_details(self):
        return self._batch_details

    @batch_details.setter
    def batch_details(self, value):
        if isinstance(value, list):
            self._batch_details = list()
            for i in value:
                if isinstance(i, CareerOpenBaseInvitationDetail):
                    self._batch_details.append(i)
                else:
                    self._batch_details.append(CareerOpenBaseInvitationDetail.from_alipay_dict(i))
    @property
    def out_batch_no(self):
        return self._out_batch_no

    @out_batch_no.setter
    def out_batch_no(self, value):
        self._out_batch_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_details:
            if isinstance(self.batch_details, list):
                for i in range(0, len(self.batch_details)):
                    element = self.batch_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.batch_details[i] = element.to_alipay_dict()
            if hasattr(self.batch_details, 'to_alipay_dict'):
                params['batch_details'] = self.batch_details.to_alipay_dict()
            else:
                params['batch_details'] = self.batch_details
        if self.out_batch_no:
            if hasattr(self.out_batch_no, 'to_alipay_dict'):
                params['out_batch_no'] = self.out_batch_no.to_alipay_dict()
            else:
                params['out_batch_no'] = self.out_batch_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCareerOpenbaseInvitationBatchsendModel()
        if 'batch_details' in d:
            o.batch_details = d['batch_details']
        if 'out_batch_no' in d:
            o.out_batch_no = d['out_batch_no']
        return o


