#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntProdpaasProductInspectionCompleteCallbackModel(object):

    def __init__(self):
        self._ao_no = None
        self._defect_reason = None
        self._feedback_time = None
        self._inspection_picture = None
        self._inspection_report_attachment = None
        self._inspection_result = None
        self._quality_inspection_no = None
        self._quantity = None
        self._result_remark = None

    @property
    def ao_no(self):
        return self._ao_no

    @ao_no.setter
    def ao_no(self, value):
        self._ao_no = value
    @property
    def defect_reason(self):
        return self._defect_reason

    @defect_reason.setter
    def defect_reason(self, value):
        self._defect_reason = value
    @property
    def feedback_time(self):
        return self._feedback_time

    @feedback_time.setter
    def feedback_time(self, value):
        self._feedback_time = value
    @property
    def inspection_picture(self):
        return self._inspection_picture

    @inspection_picture.setter
    def inspection_picture(self, value):
        self._inspection_picture = value
    @property
    def inspection_report_attachment(self):
        return self._inspection_report_attachment

    @inspection_report_attachment.setter
    def inspection_report_attachment(self, value):
        self._inspection_report_attachment = value
    @property
    def inspection_result(self):
        return self._inspection_result

    @inspection_result.setter
    def inspection_result(self, value):
        self._inspection_result = value
    @property
    def quality_inspection_no(self):
        return self._quality_inspection_no

    @quality_inspection_no.setter
    def quality_inspection_no(self, value):
        self._quality_inspection_no = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def result_remark(self):
        return self._result_remark

    @result_remark.setter
    def result_remark(self, value):
        self._result_remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.ao_no:
            if hasattr(self.ao_no, 'to_alipay_dict'):
                params['ao_no'] = self.ao_no.to_alipay_dict()
            else:
                params['ao_no'] = self.ao_no
        if self.defect_reason:
            if hasattr(self.defect_reason, 'to_alipay_dict'):
                params['defect_reason'] = self.defect_reason.to_alipay_dict()
            else:
                params['defect_reason'] = self.defect_reason
        if self.feedback_time:
            if hasattr(self.feedback_time, 'to_alipay_dict'):
                params['feedback_time'] = self.feedback_time.to_alipay_dict()
            else:
                params['feedback_time'] = self.feedback_time
        if self.inspection_picture:
            if hasattr(self.inspection_picture, 'to_alipay_dict'):
                params['inspection_picture'] = self.inspection_picture.to_alipay_dict()
            else:
                params['inspection_picture'] = self.inspection_picture
        if self.inspection_report_attachment:
            if hasattr(self.inspection_report_attachment, 'to_alipay_dict'):
                params['inspection_report_attachment'] = self.inspection_report_attachment.to_alipay_dict()
            else:
                params['inspection_report_attachment'] = self.inspection_report_attachment
        if self.inspection_result:
            if hasattr(self.inspection_result, 'to_alipay_dict'):
                params['inspection_result'] = self.inspection_result.to_alipay_dict()
            else:
                params['inspection_result'] = self.inspection_result
        if self.quality_inspection_no:
            if hasattr(self.quality_inspection_no, 'to_alipay_dict'):
                params['quality_inspection_no'] = self.quality_inspection_no.to_alipay_dict()
            else:
                params['quality_inspection_no'] = self.quality_inspection_no
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.result_remark:
            if hasattr(self.result_remark, 'to_alipay_dict'):
                params['result_remark'] = self.result_remark.to_alipay_dict()
            else:
                params['result_remark'] = self.result_remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntProdpaasProductInspectionCompleteCallbackModel()
        if 'ao_no' in d:
            o.ao_no = d['ao_no']
        if 'defect_reason' in d:
            o.defect_reason = d['defect_reason']
        if 'feedback_time' in d:
            o.feedback_time = d['feedback_time']
        if 'inspection_picture' in d:
            o.inspection_picture = d['inspection_picture']
        if 'inspection_report_attachment' in d:
            o.inspection_report_attachment = d['inspection_report_attachment']
        if 'inspection_result' in d:
            o.inspection_result = d['inspection_result']
        if 'quality_inspection_no' in d:
            o.quality_inspection_no = d['quality_inspection_no']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'result_remark' in d:
            o.result_remark = d['result_remark']
        return o


