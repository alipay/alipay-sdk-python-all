#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSchooldeviceSmSignupModel(object):

    def __init__(self):
        self._activity_code = None
        self._biz_code = None
        self._business_inner_image = None
        self._business_license_image = None
        self._business_outer_image = None
        self._cooperation_agreement_image = None
        self._legal_person_certification_image = None
        self._sm_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def business_inner_image(self):
        return self._business_inner_image

    @business_inner_image.setter
    def business_inner_image(self, value):
        if isinstance(value, list):
            self._business_inner_image = list()
            for i in value:
                self._business_inner_image.append(i)
    @property
    def business_license_image(self):
        return self._business_license_image

    @business_license_image.setter
    def business_license_image(self, value):
        if isinstance(value, list):
            self._business_license_image = list()
            for i in value:
                self._business_license_image.append(i)
    @property
    def business_outer_image(self):
        return self._business_outer_image

    @business_outer_image.setter
    def business_outer_image(self, value):
        if isinstance(value, list):
            self._business_outer_image = list()
            for i in value:
                self._business_outer_image.append(i)
    @property
    def cooperation_agreement_image(self):
        return self._cooperation_agreement_image

    @cooperation_agreement_image.setter
    def cooperation_agreement_image(self, value):
        if isinstance(value, list):
            self._cooperation_agreement_image = list()
            for i in value:
                self._cooperation_agreement_image.append(i)
    @property
    def legal_person_certification_image(self):
        return self._legal_person_certification_image

    @legal_person_certification_image.setter
    def legal_person_certification_image(self, value):
        if isinstance(value, list):
            self._legal_person_certification_image = list()
            for i in value:
                self._legal_person_certification_image.append(i)
    @property
    def sm_id(self):
        return self._sm_id

    @sm_id.setter
    def sm_id(self, value):
        self._sm_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.business_inner_image:
            if isinstance(self.business_inner_image, list):
                for i in range(0, len(self.business_inner_image)):
                    element = self.business_inner_image[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_inner_image[i] = element.to_alipay_dict()
            if hasattr(self.business_inner_image, 'to_alipay_dict'):
                params['business_inner_image'] = self.business_inner_image.to_alipay_dict()
            else:
                params['business_inner_image'] = self.business_inner_image
        if self.business_license_image:
            if isinstance(self.business_license_image, list):
                for i in range(0, len(self.business_license_image)):
                    element = self.business_license_image[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_license_image[i] = element.to_alipay_dict()
            if hasattr(self.business_license_image, 'to_alipay_dict'):
                params['business_license_image'] = self.business_license_image.to_alipay_dict()
            else:
                params['business_license_image'] = self.business_license_image
        if self.business_outer_image:
            if isinstance(self.business_outer_image, list):
                for i in range(0, len(self.business_outer_image)):
                    element = self.business_outer_image[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_outer_image[i] = element.to_alipay_dict()
            if hasattr(self.business_outer_image, 'to_alipay_dict'):
                params['business_outer_image'] = self.business_outer_image.to_alipay_dict()
            else:
                params['business_outer_image'] = self.business_outer_image
        if self.cooperation_agreement_image:
            if isinstance(self.cooperation_agreement_image, list):
                for i in range(0, len(self.cooperation_agreement_image)):
                    element = self.cooperation_agreement_image[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cooperation_agreement_image[i] = element.to_alipay_dict()
            if hasattr(self.cooperation_agreement_image, 'to_alipay_dict'):
                params['cooperation_agreement_image'] = self.cooperation_agreement_image.to_alipay_dict()
            else:
                params['cooperation_agreement_image'] = self.cooperation_agreement_image
        if self.legal_person_certification_image:
            if isinstance(self.legal_person_certification_image, list):
                for i in range(0, len(self.legal_person_certification_image)):
                    element = self.legal_person_certification_image[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.legal_person_certification_image[i] = element.to_alipay_dict()
            if hasattr(self.legal_person_certification_image, 'to_alipay_dict'):
                params['legal_person_certification_image'] = self.legal_person_certification_image.to_alipay_dict()
            else:
                params['legal_person_certification_image'] = self.legal_person_certification_image
        if self.sm_id:
            if hasattr(self.sm_id, 'to_alipay_dict'):
                params['sm_id'] = self.sm_id.to_alipay_dict()
            else:
                params['sm_id'] = self.sm_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSchooldeviceSmSignupModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'business_inner_image' in d:
            o.business_inner_image = d['business_inner_image']
        if 'business_license_image' in d:
            o.business_license_image = d['business_license_image']
        if 'business_outer_image' in d:
            o.business_outer_image = d['business_outer_image']
        if 'cooperation_agreement_image' in d:
            o.cooperation_agreement_image = d['cooperation_agreement_image']
        if 'legal_person_certification_image' in d:
            o.legal_person_certification_image = d['legal_person_certification_image']
        if 'sm_id' in d:
            o.sm_id = d['sm_id']
        return o


