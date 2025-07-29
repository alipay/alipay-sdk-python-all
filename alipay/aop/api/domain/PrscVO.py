#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrescReview import PrescReview


class PrscVO(object):

    def __init__(self):
        self._channel = None
        self._create_time = None
        self._gender = None
        self._patient_age = None
        self._patient_id_no = None
        self._patient_name = None
        self._patient_phone_no = None
        self._prescri_review = None
        self._prsc_biz_type = None
        self._rx_code = None
        self._rx_doc_name = None
        self._rx_id = None
        self._rx_pdf = None
        self._rx_picture = None
        self._rx_status = None
        self._seller_key = None
        self._store_code = None
        self._update_time = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def patient_age(self):
        return self._patient_age

    @patient_age.setter
    def patient_age(self, value):
        self._patient_age = value
    @property
    def patient_id_no(self):
        return self._patient_id_no

    @patient_id_no.setter
    def patient_id_no(self, value):
        self._patient_id_no = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def patient_phone_no(self):
        return self._patient_phone_no

    @patient_phone_no.setter
    def patient_phone_no(self, value):
        self._patient_phone_no = value
    @property
    def prescri_review(self):
        return self._prescri_review

    @prescri_review.setter
    def prescri_review(self, value):
        if isinstance(value, PrescReview):
            self._prescri_review = value
        else:
            self._prescri_review = PrescReview.from_alipay_dict(value)
    @property
    def prsc_biz_type(self):
        return self._prsc_biz_type

    @prsc_biz_type.setter
    def prsc_biz_type(self, value):
        self._prsc_biz_type = value
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
    def rx_id(self):
        return self._rx_id

    @rx_id.setter
    def rx_id(self, value):
        self._rx_id = value
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
    def seller_key(self):
        return self._seller_key

    @seller_key.setter
    def seller_key(self, value):
        self._seller_key = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.patient_age:
            if hasattr(self.patient_age, 'to_alipay_dict'):
                params['patient_age'] = self.patient_age.to_alipay_dict()
            else:
                params['patient_age'] = self.patient_age
        if self.patient_id_no:
            if hasattr(self.patient_id_no, 'to_alipay_dict'):
                params['patient_id_no'] = self.patient_id_no.to_alipay_dict()
            else:
                params['patient_id_no'] = self.patient_id_no
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.patient_phone_no:
            if hasattr(self.patient_phone_no, 'to_alipay_dict'):
                params['patient_phone_no'] = self.patient_phone_no.to_alipay_dict()
            else:
                params['patient_phone_no'] = self.patient_phone_no
        if self.prescri_review:
            if hasattr(self.prescri_review, 'to_alipay_dict'):
                params['prescri_review'] = self.prescri_review.to_alipay_dict()
            else:
                params['prescri_review'] = self.prescri_review
        if self.prsc_biz_type:
            if hasattr(self.prsc_biz_type, 'to_alipay_dict'):
                params['prsc_biz_type'] = self.prsc_biz_type.to_alipay_dict()
            else:
                params['prsc_biz_type'] = self.prsc_biz_type
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
        if self.rx_id:
            if hasattr(self.rx_id, 'to_alipay_dict'):
                params['rx_id'] = self.rx_id.to_alipay_dict()
            else:
                params['rx_id'] = self.rx_id
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
        if self.seller_key:
            if hasattr(self.seller_key, 'to_alipay_dict'):
                params['seller_key'] = self.seller_key.to_alipay_dict()
            else:
                params['seller_key'] = self.seller_key
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
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
        o = PrscVO()
        if 'channel' in d:
            o.channel = d['channel']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'gender' in d:
            o.gender = d['gender']
        if 'patient_age' in d:
            o.patient_age = d['patient_age']
        if 'patient_id_no' in d:
            o.patient_id_no = d['patient_id_no']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'patient_phone_no' in d:
            o.patient_phone_no = d['patient_phone_no']
        if 'prescri_review' in d:
            o.prescri_review = d['prescri_review']
        if 'prsc_biz_type' in d:
            o.prsc_biz_type = d['prsc_biz_type']
        if 'rx_code' in d:
            o.rx_code = d['rx_code']
        if 'rx_doc_name' in d:
            o.rx_doc_name = d['rx_doc_name']
        if 'rx_id' in d:
            o.rx_id = d['rx_id']
        if 'rx_pdf' in d:
            o.rx_pdf = d['rx_pdf']
        if 'rx_picture' in d:
            o.rx_picture = d['rx_picture']
        if 'rx_status' in d:
            o.rx_status = d['rx_status']
        if 'seller_key' in d:
            o.seller_key = d['seller_key']
        if 'store_code' in d:
            o.store_code = d['store_code']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


