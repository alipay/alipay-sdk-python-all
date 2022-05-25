#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApplyAttatchmentVO(object):

    def __init__(self):
        self._apply_doc = None
        self._auth_docs = None
        self._bid_doc = None
        self._business_licenses = None
        self._corporation_cert = None
        self._entrust_doc = None
        self._legal_person_cert = None

    @property
    def apply_doc(self):
        return self._apply_doc

    @apply_doc.setter
    def apply_doc(self, value):
        self._apply_doc = value
    @property
    def auth_docs(self):
        return self._auth_docs

    @auth_docs.setter
    def auth_docs(self, value):
        self._auth_docs = value
    @property
    def bid_doc(self):
        return self._bid_doc

    @bid_doc.setter
    def bid_doc(self, value):
        self._bid_doc = value
    @property
    def business_licenses(self):
        return self._business_licenses

    @business_licenses.setter
    def business_licenses(self, value):
        self._business_licenses = value
    @property
    def corporation_cert(self):
        return self._corporation_cert

    @corporation_cert.setter
    def corporation_cert(self, value):
        self._corporation_cert = value
    @property
    def entrust_doc(self):
        return self._entrust_doc

    @entrust_doc.setter
    def entrust_doc(self, value):
        self._entrust_doc = value
    @property
    def legal_person_cert(self):
        return self._legal_person_cert

    @legal_person_cert.setter
    def legal_person_cert(self, value):
        self._legal_person_cert = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_doc:
            if hasattr(self.apply_doc, 'to_alipay_dict'):
                params['apply_doc'] = self.apply_doc.to_alipay_dict()
            else:
                params['apply_doc'] = self.apply_doc
        if self.auth_docs:
            if hasattr(self.auth_docs, 'to_alipay_dict'):
                params['auth_docs'] = self.auth_docs.to_alipay_dict()
            else:
                params['auth_docs'] = self.auth_docs
        if self.bid_doc:
            if hasattr(self.bid_doc, 'to_alipay_dict'):
                params['bid_doc'] = self.bid_doc.to_alipay_dict()
            else:
                params['bid_doc'] = self.bid_doc
        if self.business_licenses:
            if hasattr(self.business_licenses, 'to_alipay_dict'):
                params['business_licenses'] = self.business_licenses.to_alipay_dict()
            else:
                params['business_licenses'] = self.business_licenses
        if self.corporation_cert:
            if hasattr(self.corporation_cert, 'to_alipay_dict'):
                params['corporation_cert'] = self.corporation_cert.to_alipay_dict()
            else:
                params['corporation_cert'] = self.corporation_cert
        if self.entrust_doc:
            if hasattr(self.entrust_doc, 'to_alipay_dict'):
                params['entrust_doc'] = self.entrust_doc.to_alipay_dict()
            else:
                params['entrust_doc'] = self.entrust_doc
        if self.legal_person_cert:
            if hasattr(self.legal_person_cert, 'to_alipay_dict'):
                params['legal_person_cert'] = self.legal_person_cert.to_alipay_dict()
            else:
                params['legal_person_cert'] = self.legal_person_cert
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyAttatchmentVO()
        if 'apply_doc' in d:
            o.apply_doc = d['apply_doc']
        if 'auth_docs' in d:
            o.auth_docs = d['auth_docs']
        if 'bid_doc' in d:
            o.bid_doc = d['bid_doc']
        if 'business_licenses' in d:
            o.business_licenses = d['business_licenses']
        if 'corporation_cert' in d:
            o.corporation_cert = d['corporation_cert']
        if 'entrust_doc' in d:
            o.entrust_doc = d['entrust_doc']
        if 'legal_person_cert' in d:
            o.legal_person_cert = d['legal_person_cert']
        return o


