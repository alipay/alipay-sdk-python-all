#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantCard import MerchantCard


class AlipayMarketingCardTransferCreateModel(object):

    def __init__(self):
        self._card_info = None
        self._occur_time = None
        self._out_serial_no = None
        self._source_pid = None
        self._source_template_id = None
        self._target_card_no = None
        self._target_card_no_type = None

    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, MerchantCard):
            self._card_info = value
        else:
            self._card_info = MerchantCard.from_alipay_dict(value)
    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def source_pid(self):
        return self._source_pid

    @source_pid.setter
    def source_pid(self, value):
        self._source_pid = value
    @property
    def source_template_id(self):
        return self._source_template_id

    @source_template_id.setter
    def source_template_id(self, value):
        self._source_template_id = value
    @property
    def target_card_no(self):
        return self._target_card_no

    @target_card_no.setter
    def target_card_no(self, value):
        self._target_card_no = value
    @property
    def target_card_no_type(self):
        return self._target_card_no_type

    @target_card_no_type.setter
    def target_card_no_type(self, value):
        self._target_card_no_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_info:
            if hasattr(self.card_info, 'to_alipay_dict'):
                params['card_info'] = self.card_info.to_alipay_dict()
            else:
                params['card_info'] = self.card_info
        if self.occur_time:
            if hasattr(self.occur_time, 'to_alipay_dict'):
                params['occur_time'] = self.occur_time.to_alipay_dict()
            else:
                params['occur_time'] = self.occur_time
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.source_pid:
            if hasattr(self.source_pid, 'to_alipay_dict'):
                params['source_pid'] = self.source_pid.to_alipay_dict()
            else:
                params['source_pid'] = self.source_pid
        if self.source_template_id:
            if hasattr(self.source_template_id, 'to_alipay_dict'):
                params['source_template_id'] = self.source_template_id.to_alipay_dict()
            else:
                params['source_template_id'] = self.source_template_id
        if self.target_card_no:
            if hasattr(self.target_card_no, 'to_alipay_dict'):
                params['target_card_no'] = self.target_card_no.to_alipay_dict()
            else:
                params['target_card_no'] = self.target_card_no
        if self.target_card_no_type:
            if hasattr(self.target_card_no_type, 'to_alipay_dict'):
                params['target_card_no_type'] = self.target_card_no_type.to_alipay_dict()
            else:
                params['target_card_no_type'] = self.target_card_no_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardTransferCreateModel()
        if 'card_info' in d:
            o.card_info = d['card_info']
        if 'occur_time' in d:
            o.occur_time = d['occur_time']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'source_pid' in d:
            o.source_pid = d['source_pid']
        if 'source_template_id' in d:
            o.source_template_id = d['source_template_id']
        if 'target_card_no' in d:
            o.target_card_no = d['target_card_no']
        if 'target_card_no_type' in d:
            o.target_card_no_type = d['target_card_no_type']
        return o


