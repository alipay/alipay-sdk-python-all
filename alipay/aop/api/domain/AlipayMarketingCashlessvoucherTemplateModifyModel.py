#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCashlessvoucherTemplateModifyModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._publish_end_time = None
        self._rule_conf = None
        self._template_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def rule_conf(self):
        return self._rule_conf

    @rule_conf.setter
    def rule_conf(self, value):
        self._rule_conf = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.rule_conf:
            if hasattr(self.rule_conf, 'to_alipay_dict'):
                params['rule_conf'] = self.rule_conf.to_alipay_dict()
            else:
                params['rule_conf'] = self.rule_conf
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCashlessvoucherTemplateModifyModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'rule_conf' in d:
            o.rule_conf = d['rule_conf']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


