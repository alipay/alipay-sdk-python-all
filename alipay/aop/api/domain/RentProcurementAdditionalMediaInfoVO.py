#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentProcurementAdditionalMediaInfoVO(object):

    def __init__(self):
        self._electronic_signature_url = None
        self._electronic_stub_url = None
        self._face_active_url_list = None
        self._face_document_url = None
        self._face_sign_url = None
        self._route_tracking_url = None

    @property
    def electronic_signature_url(self):
        return self._electronic_signature_url

    @electronic_signature_url.setter
    def electronic_signature_url(self, value):
        self._electronic_signature_url = value
    @property
    def electronic_stub_url(self):
        return self._electronic_stub_url

    @electronic_stub_url.setter
    def electronic_stub_url(self, value):
        self._electronic_stub_url = value
    @property
    def face_active_url_list(self):
        return self._face_active_url_list

    @face_active_url_list.setter
    def face_active_url_list(self, value):
        if isinstance(value, list):
            self._face_active_url_list = list()
            for i in value:
                self._face_active_url_list.append(i)
    @property
    def face_document_url(self):
        return self._face_document_url

    @face_document_url.setter
    def face_document_url(self, value):
        self._face_document_url = value
    @property
    def face_sign_url(self):
        return self._face_sign_url

    @face_sign_url.setter
    def face_sign_url(self, value):
        self._face_sign_url = value
    @property
    def route_tracking_url(self):
        return self._route_tracking_url

    @route_tracking_url.setter
    def route_tracking_url(self, value):
        self._route_tracking_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.electronic_signature_url:
            if hasattr(self.electronic_signature_url, 'to_alipay_dict'):
                params['electronic_signature_url'] = self.electronic_signature_url.to_alipay_dict()
            else:
                params['electronic_signature_url'] = self.electronic_signature_url
        if self.electronic_stub_url:
            if hasattr(self.electronic_stub_url, 'to_alipay_dict'):
                params['electronic_stub_url'] = self.electronic_stub_url.to_alipay_dict()
            else:
                params['electronic_stub_url'] = self.electronic_stub_url
        if self.face_active_url_list:
            if isinstance(self.face_active_url_list, list):
                for i in range(0, len(self.face_active_url_list)):
                    element = self.face_active_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.face_active_url_list[i] = element.to_alipay_dict()
            if hasattr(self.face_active_url_list, 'to_alipay_dict'):
                params['face_active_url_list'] = self.face_active_url_list.to_alipay_dict()
            else:
                params['face_active_url_list'] = self.face_active_url_list
        if self.face_document_url:
            if hasattr(self.face_document_url, 'to_alipay_dict'):
                params['face_document_url'] = self.face_document_url.to_alipay_dict()
            else:
                params['face_document_url'] = self.face_document_url
        if self.face_sign_url:
            if hasattr(self.face_sign_url, 'to_alipay_dict'):
                params['face_sign_url'] = self.face_sign_url.to_alipay_dict()
            else:
                params['face_sign_url'] = self.face_sign_url
        if self.route_tracking_url:
            if hasattr(self.route_tracking_url, 'to_alipay_dict'):
                params['route_tracking_url'] = self.route_tracking_url.to_alipay_dict()
            else:
                params['route_tracking_url'] = self.route_tracking_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentProcurementAdditionalMediaInfoVO()
        if 'electronic_signature_url' in d:
            o.electronic_signature_url = d['electronic_signature_url']
        if 'electronic_stub_url' in d:
            o.electronic_stub_url = d['electronic_stub_url']
        if 'face_active_url_list' in d:
            o.face_active_url_list = d['face_active_url_list']
        if 'face_document_url' in d:
            o.face_document_url = d['face_document_url']
        if 'face_sign_url' in d:
            o.face_sign_url = d['face_sign_url']
        if 'route_tracking_url' in d:
            o.route_tracking_url = d['route_tracking_url']
        return o


