#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WorkListVO(object):

    def __init__(self):
        self._gmt_finished = None
        self._notice_out_biz_no = None
        self._notice_out_biz_type = None
        self._operator = None
        self._status = None
        self._warehouse_code = None
        self._work_id = None
        self._work_type = None

    @property
    def gmt_finished(self):
        return self._gmt_finished

    @gmt_finished.setter
    def gmt_finished(self, value):
        self._gmt_finished = value
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
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
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
    def work_id(self):
        return self._work_id

    @work_id.setter
    def work_id(self, value):
        self._work_id = value
    @property
    def work_type(self):
        return self._work_type

    @work_type.setter
    def work_type(self, value):
        self._work_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_finished:
            if hasattr(self.gmt_finished, 'to_alipay_dict'):
                params['gmt_finished'] = self.gmt_finished.to_alipay_dict()
            else:
                params['gmt_finished'] = self.gmt_finished
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
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
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
        if self.work_id:
            if hasattr(self.work_id, 'to_alipay_dict'):
                params['work_id'] = self.work_id.to_alipay_dict()
            else:
                params['work_id'] = self.work_id
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
        o = WorkListVO()
        if 'gmt_finished' in d:
            o.gmt_finished = d['gmt_finished']
        if 'notice_out_biz_no' in d:
            o.notice_out_biz_no = d['notice_out_biz_no']
        if 'notice_out_biz_type' in d:
            o.notice_out_biz_type = d['notice_out_biz_type']
        if 'operator' in d:
            o.operator = d['operator']
        if 'status' in d:
            o.status = d['status']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        if 'work_id' in d:
            o.work_id = d['work_id']
        if 'work_type' in d:
            o.work_type = d['work_type']
        return o


