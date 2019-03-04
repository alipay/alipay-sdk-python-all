#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetSubFeedbackInfo import AssetSubFeedbackInfo


class AssetResult(object):

    def __init__(self):
        self._assign_item_id = None
        self._batch_no = None
        self._error_code = None
        self._error_desc = None
        self._request_id = None
        self._sub_feedback_infos = None
        self._success = None

    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sub_feedback_infos(self):
        return self._sub_feedback_infos

    @sub_feedback_infos.setter
    def sub_feedback_infos(self, value):
        if isinstance(value, list):
            self._sub_feedback_infos = list()
            for i in value:
                if isinstance(i, AssetSubFeedbackInfo):
                    self._sub_feedback_infos.append(i)
                else:
                    self._sub_feedback_infos.append(AssetSubFeedbackInfo.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_desc:
            if hasattr(self.error_desc, 'to_alipay_dict'):
                params['error_desc'] = self.error_desc.to_alipay_dict()
            else:
                params['error_desc'] = self.error_desc
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sub_feedback_infos:
            if isinstance(self.sub_feedback_infos, list):
                for i in range(0, len(self.sub_feedback_infos)):
                    element = self.sub_feedback_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_feedback_infos[i] = element.to_alipay_dict()
            if hasattr(self.sub_feedback_infos, 'to_alipay_dict'):
                params['sub_feedback_infos'] = self.sub_feedback_infos.to_alipay_dict()
            else:
                params['sub_feedback_infos'] = self.sub_feedback_infos
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetResult()
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_desc' in d:
            o.error_desc = d['error_desc']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sub_feedback_infos' in d:
            o.sub_feedback_infos = d['sub_feedback_infos']
        if 'success' in d:
            o.success = d['success']
        return o


