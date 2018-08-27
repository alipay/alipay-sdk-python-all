#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsDeliverypackageQueryModel(object):

    def __init__(self):
        self._express_code = None
        self._notice_order_id = None
        self._operate_context = None
        self._work_order_id = None

    @property
    def express_code(self):
        return self._express_code

    @express_code.setter
    def express_code(self, value):
        self._express_code = value
    @property
    def notice_order_id(self):
        return self._notice_order_id

    @notice_order_id.setter
    def notice_order_id(self, value):
        self._notice_order_id = value
    @property
    def operate_context(self):
        return self._operate_context

    @operate_context.setter
    def operate_context(self, value):
        if isinstance(value, OperateContext):
            self._operate_context = value
        else:
            self._operate_context = OperateContext.from_alipay_dict(value)
    @property
    def work_order_id(self):
        return self._work_order_id

    @work_order_id.setter
    def work_order_id(self, value):
        self._work_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_code:
            if hasattr(self.express_code, 'to_alipay_dict'):
                params['express_code'] = self.express_code.to_alipay_dict()
            else:
                params['express_code'] = self.express_code
        if self.notice_order_id:
            if hasattr(self.notice_order_id, 'to_alipay_dict'):
                params['notice_order_id'] = self.notice_order_id.to_alipay_dict()
            else:
                params['notice_order_id'] = self.notice_order_id
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.work_order_id:
            if hasattr(self.work_order_id, 'to_alipay_dict'):
                params['work_order_id'] = self.work_order_id.to_alipay_dict()
            else:
                params['work_order_id'] = self.work_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsDeliverypackageQueryModel()
        if 'express_code' in d:
            o.express_code = d['express_code']
        if 'notice_order_id' in d:
            o.notice_order_id = d['notice_order_id']
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'work_order_id' in d:
            o.work_order_id = d['work_order_id']
        return o


