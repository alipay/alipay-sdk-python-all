#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrescriptionVO(object):

    def __init__(self):
        self._create_time = None
        self._review_doc_name = None
        self._review_reject_note = None
        self._review_time = None
        self._rx_code = None
        self._rx_doc_name = None
        self._rx_pdf = None
        self._rx_picture = None
        self._rx_status = None
        self._update_time = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def review_doc_name(self):
        return self._review_doc_name

    @review_doc_name.setter
    def review_doc_name(self, value):
        self._review_doc_name = value
    @property
    def review_reject_note(self):
        return self._review_reject_note

    @review_reject_note.setter
    def review_reject_note(self, value):
        self._review_reject_note = value
    @property
    def review_time(self):
        return self._review_time

    @review_time.setter
    def review_time(self, value):
        self._review_time = value
    @property
    def rx_code(self):
        return self._rx_code

    @rx_code.setter
    def rx_code(self, value):
        self._rx_code = value
    @property
    def rx_doc_name(self):
        return self._rx_doc_name

    @rx_doc_name.setter
    def rx_doc_name(self, value):
        self._rx_doc_name = value
    @property
    def rx_pdf(self):
        return self._rx_pdf

    @rx_pdf.setter
    def rx_pdf(self, value):
        self._rx_pdf = value
    @property
    def rx_picture(self):
        return self._rx_picture

    @rx_picture.setter
    def rx_picture(self, value):
        self._rx_picture = value
    @property
    def rx_status(self):
        return self._rx_status

    @rx_status.setter
    def rx_status(self, value):
        self._rx_status = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.review_doc_name:
            if hasattr(self.review_doc_name, 'to_alipay_dict'):
                params['review_doc_name'] = self.review_doc_name.to_alipay_dict()
            else:
                params['review_doc_name'] = self.review_doc_name
        if self.review_reject_note:
            if hasattr(self.review_reject_note, 'to_alipay_dict'):
                params['review_reject_note'] = self.review_reject_note.to_alipay_dict()
            else:
                params['review_reject_note'] = self.review_reject_note
        if self.review_time:
            if hasattr(self.review_time, 'to_alipay_dict'):
                params['review_time'] = self.review_time.to_alipay_dict()
            else:
                params['review_time'] = self.review_time
        if self.rx_code:
            if hasattr(self.rx_code, 'to_alipay_dict'):
                params['rx_code'] = self.rx_code.to_alipay_dict()
            else:
                params['rx_code'] = self.rx_code
        if self.rx_doc_name:
            if hasattr(self.rx_doc_name, 'to_alipay_dict'):
                params['rx_doc_name'] = self.rx_doc_name.to_alipay_dict()
            else:
                params['rx_doc_name'] = self.rx_doc_name
        if self.rx_pdf:
            if hasattr(self.rx_pdf, 'to_alipay_dict'):
                params['rx_pdf'] = self.rx_pdf.to_alipay_dict()
            else:
                params['rx_pdf'] = self.rx_pdf
        if self.rx_picture:
            if hasattr(self.rx_picture, 'to_alipay_dict'):
                params['rx_picture'] = self.rx_picture.to_alipay_dict()
            else:
                params['rx_picture'] = self.rx_picture
        if self.rx_status:
            if hasattr(self.rx_status, 'to_alipay_dict'):
                params['rx_status'] = self.rx_status.to_alipay_dict()
            else:
                params['rx_status'] = self.rx_status
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrescriptionVO()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'review_doc_name' in d:
            o.review_doc_name = d['review_doc_name']
        if 'review_reject_note' in d:
            o.review_reject_note = d['review_reject_note']
        if 'review_time' in d:
            o.review_time = d['review_time']
        if 'rx_code' in d:
            o.rx_code = d['rx_code']
        if 'rx_doc_name' in d:
            o.rx_doc_name = d['rx_doc_name']
        if 'rx_pdf' in d:
            o.rx_pdf = d['rx_pdf']
        if 'rx_picture' in d:
            o.rx_picture = d['rx_picture']
        if 'rx_status' in d:
            o.rx_status = d['rx_status']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


