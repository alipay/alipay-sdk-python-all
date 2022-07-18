#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessRelationApplyTargetInfo import BusinessRelationApplyTargetInfo
from alipay.aop.api.domain.BusinessRelationAttachmentInfo import BusinessRelationAttachmentInfo


class AlipayBusinessRelationProductApplyModel(object):

    def __init__(self):
        self._apply_target_info = None
        self._attachment_info = None
        self._biz_no = None
        self._group_id = None
        self._group_sub_type = None
        self._group_type = None
        self._operation_type = None
        self._out_biz_no = None
        self._product_code = None

    @property
    def apply_target_info(self):
        return self._apply_target_info

    @apply_target_info.setter
    def apply_target_info(self, value):
        if isinstance(value, BusinessRelationApplyTargetInfo):
            self._apply_target_info = value
        else:
            self._apply_target_info = BusinessRelationApplyTargetInfo.from_alipay_dict(value)
    @property
    def attachment_info(self):
        return self._attachment_info

    @attachment_info.setter
    def attachment_info(self, value):
        if isinstance(value, BusinessRelationAttachmentInfo):
            self._attachment_info = value
        else:
            self._attachment_info = BusinessRelationAttachmentInfo.from_alipay_dict(value)
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_sub_type(self):
        return self._group_sub_type

    @group_sub_type.setter
    def group_sub_type(self, value):
        self._group_sub_type = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_target_info:
            if hasattr(self.apply_target_info, 'to_alipay_dict'):
                params['apply_target_info'] = self.apply_target_info.to_alipay_dict()
            else:
                params['apply_target_info'] = self.apply_target_info
        if self.attachment_info:
            if hasattr(self.attachment_info, 'to_alipay_dict'):
                params['attachment_info'] = self.attachment_info.to_alipay_dict()
            else:
                params['attachment_info'] = self.attachment_info
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_sub_type:
            if hasattr(self.group_sub_type, 'to_alipay_dict'):
                params['group_sub_type'] = self.group_sub_type.to_alipay_dict()
            else:
                params['group_sub_type'] = self.group_sub_type
        if self.group_type:
            if hasattr(self.group_type, 'to_alipay_dict'):
                params['group_type'] = self.group_type.to_alipay_dict()
            else:
                params['group_type'] = self.group_type
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessRelationProductApplyModel()
        if 'apply_target_info' in d:
            o.apply_target_info = d['apply_target_info']
        if 'attachment_info' in d:
            o.attachment_info = d['attachment_info']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_sub_type' in d:
            o.group_sub_type = d['group_sub_type']
        if 'group_type' in d:
            o.group_type = d['group_type']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


