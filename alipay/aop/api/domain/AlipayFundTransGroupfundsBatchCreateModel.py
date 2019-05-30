#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupFundsImcomeDetails import GroupFundsImcomeDetails


class AlipayFundTransGroupfundsBatchCreateModel(object):

    def __init__(self):
        self._current_user_id = None
        self._ext_param = None
        self._income_details = None
        self._out_biz_no = None
        self._source = None
        self._total_amount = None

    @property
    def current_user_id(self):
        return self._current_user_id

    @current_user_id.setter
    def current_user_id(self, value):
        self._current_user_id = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def income_details(self):
        return self._income_details

    @income_details.setter
    def income_details(self, value):
        if isinstance(value, list):
            self._income_details = list()
            for i in value:
                if isinstance(i, GroupFundsImcomeDetails):
                    self._income_details.append(i)
                else:
                    self._income_details.append(GroupFundsImcomeDetails.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_user_id:
            if hasattr(self.current_user_id, 'to_alipay_dict'):
                params['current_user_id'] = self.current_user_id.to_alipay_dict()
            else:
                params['current_user_id'] = self.current_user_id
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.income_details:
            if isinstance(self.income_details, list):
                for i in range(0, len(self.income_details)):
                    element = self.income_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.income_details[i] = element.to_alipay_dict()
            if hasattr(self.income_details, 'to_alipay_dict'):
                params['income_details'] = self.income_details.to_alipay_dict()
            else:
                params['income_details'] = self.income_details
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransGroupfundsBatchCreateModel()
        if 'current_user_id' in d:
            o.current_user_id = d['current_user_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'income_details' in d:
            o.income_details = d['income_details']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'source' in d:
            o.source = d['source']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


