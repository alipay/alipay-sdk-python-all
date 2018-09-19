#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperateContext import OperateContext


class KoubeiRetailWmsWorkBatchqueryModel(object):

    def __init__(self):
        self._gmt_finished_from = None
        self._gmt_finished_to = None
        self._notice_out_biz_no = None
        self._notice_out_biz_type = None
        self._operate_context = None
        self._operator = None
        self._page_no = None
        self._page_size = None
        self._status = None
        self._warehouse_code = None
        self._work_type = None

    @property
    def gmt_finished_from(self):
        return self._gmt_finished_from

    @gmt_finished_from.setter
    def gmt_finished_from(self, value):
        self._gmt_finished_from = value
    @property
    def gmt_finished_to(self):
        return self._gmt_finished_to

    @gmt_finished_to.setter
    def gmt_finished_to(self, value):
        self._gmt_finished_to = value
    @property
    def notice_out_biz_no(self):
        return self._notice_out_biz_no

    @notice_out_biz_no.setter
    def notice_out_biz_no(self, value):
        self._notice_out_biz_no = value
    @property
    def notice_out_biz_type(self):
        return self._notice_out_biz_type

    @notice_out_biz_type.setter
    def notice_out_biz_type(self, value):
        self._notice_out_biz_type = value
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
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
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
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value
    @property
    def work_type(self):
        return self._work_type

    @work_type.setter
    def work_type(self, value):
        self._work_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_finished_from:
            if hasattr(self.gmt_finished_from, 'to_alipay_dict'):
                params['gmt_finished_from'] = self.gmt_finished_from.to_alipay_dict()
            else:
                params['gmt_finished_from'] = self.gmt_finished_from
        if self.gmt_finished_to:
            if hasattr(self.gmt_finished_to, 'to_alipay_dict'):
                params['gmt_finished_to'] = self.gmt_finished_to.to_alipay_dict()
            else:
                params['gmt_finished_to'] = self.gmt_finished_to
        if self.notice_out_biz_no:
            if hasattr(self.notice_out_biz_no, 'to_alipay_dict'):
                params['notice_out_biz_no'] = self.notice_out_biz_no.to_alipay_dict()
            else:
                params['notice_out_biz_no'] = self.notice_out_biz_no
        if self.notice_out_biz_type:
            if hasattr(self.notice_out_biz_type, 'to_alipay_dict'):
                params['notice_out_biz_type'] = self.notice_out_biz_type.to_alipay_dict()
            else:
                params['notice_out_biz_type'] = self.notice_out_biz_type
        if self.operate_context:
            if hasattr(self.operate_context, 'to_alipay_dict'):
                params['operate_context'] = self.operate_context.to_alipay_dict()
            else:
                params['operate_context'] = self.operate_context
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
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
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        if self.work_type:
            if hasattr(self.work_type, 'to_alipay_dict'):
                params['work_type'] = self.work_type.to_alipay_dict()
            else:
                params['work_type'] = self.work_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsWorkBatchqueryModel()
        if 'gmt_finished_from' in d:
            o.gmt_finished_from = d['gmt_finished_from']
        if 'gmt_finished_to' in d:
            o.gmt_finished_to = d['gmt_finished_to']
        if 'notice_out_biz_no' in d:
            o.notice_out_biz_no = d['notice_out_biz_no']
        if 'notice_out_biz_type' in d:
            o.notice_out_biz_type = d['notice_out_biz_type']
        if 'operate_context' in d:
            o.operate_context = d['operate_context']
        if 'operator' in d:
            o.operator = d['operator']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status' in d:
            o.status = d['status']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        if 'work_type' in d:
            o.work_type = d['work_type']
        return o


