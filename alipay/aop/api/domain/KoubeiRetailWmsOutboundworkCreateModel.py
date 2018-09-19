#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext
from alipay.aop.api.domain.WorkDetail import WorkDetail


class KoubeiRetailWmsOutboundworkCreateModel(object):

    def __init__(self):
        self._ext_info = None
        self._notice_order_id = None
        self._operate_context = None
        self._out_biz_no = None
        self._remark = None
        self._work_details = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def work_details(self):
        return self._work_details

    @work_details.setter
    def work_details(self, value):
        if isinstance(value, list):
            self._work_details = list()
            for i in value:
                if isinstance(i, WorkDetail):
                    self._work_details.append(i)
                else:
                    self._work_details.append(WorkDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.work_details:
            if isinstance(self.work_details, list):
                for i in range(0, len(self.work_details)):
                    element = self.work_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_details[i] = element.to_alipay_dict()
            if hasattr(self.work_details, 'to_alipay_dict'):
                params['work_details'] = self.work_details.to_alipay_dict()
            else:
                params['work_details'] = self.work_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsOutboundworkCreateModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'notice_order_id' in d:
            o.notice_order_id = d['notice_order_id']
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'remark' in d:
            o.remark = d['remark']
        if 'work_details' in d:
            o.work_details = d['work_details']
        return o


