#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertFields import CertFields


class CertAuditResult(object):

    def __init__(self):
        self._authority_check_retcode = None
        self._authority_check_retmessage = None
        self._authority_check_suggest = None
        self._cert_face_suggest = None
        self._compliance_suggest = None
        self._ocr = None
        self._ocr_check_suggest = None

    @property
    def authority_check_retcode(self):
        return self._authority_check_retcode

    @authority_check_retcode.setter
    def authority_check_retcode(self, value):
        self._authority_check_retcode = value
    @property
    def authority_check_retmessage(self):
        return self._authority_check_retmessage

    @authority_check_retmessage.setter
    def authority_check_retmessage(self, value):
        self._authority_check_retmessage = value
    @property
    def authority_check_suggest(self):
        return self._authority_check_suggest

    @authority_check_suggest.setter
    def authority_check_suggest(self, value):
        self._authority_check_suggest = value
    @property
    def cert_face_suggest(self):
        return self._cert_face_suggest

    @cert_face_suggest.setter
    def cert_face_suggest(self, value):
        self._cert_face_suggest = value
    @property
    def compliance_suggest(self):
        return self._compliance_suggest

    @compliance_suggest.setter
    def compliance_suggest(self, value):
        self._compliance_suggest = value
    @property
    def ocr(self):
        return self._ocr

    @ocr.setter
    def ocr(self, value):
        if isinstance(value, CertFields):
            self._ocr = value
        else:
            self._ocr = CertFields.from_alipay_dict(value)
    @property
    def ocr_check_suggest(self):
        return self._ocr_check_suggest

    @ocr_check_suggest.setter
    def ocr_check_suggest(self, value):
        self._ocr_check_suggest = value


    def to_alipay_dict(self):
        params = dict()
        if self.authority_check_retcode:
            if hasattr(self.authority_check_retcode, 'to_alipay_dict'):
                params['authority_check_retcode'] = self.authority_check_retcode.to_alipay_dict()
            else:
                params['authority_check_retcode'] = self.authority_check_retcode
        if self.authority_check_retmessage:
            if hasattr(self.authority_check_retmessage, 'to_alipay_dict'):
                params['authority_check_retmessage'] = self.authority_check_retmessage.to_alipay_dict()
            else:
                params['authority_check_retmessage'] = self.authority_check_retmessage
        if self.authority_check_suggest:
            if hasattr(self.authority_check_suggest, 'to_alipay_dict'):
                params['authority_check_suggest'] = self.authority_check_suggest.to_alipay_dict()
            else:
                params['authority_check_suggest'] = self.authority_check_suggest
        if self.cert_face_suggest:
            if hasattr(self.cert_face_suggest, 'to_alipay_dict'):
                params['cert_face_suggest'] = self.cert_face_suggest.to_alipay_dict()
            else:
                params['cert_face_suggest'] = self.cert_face_suggest
        if self.compliance_suggest:
            if hasattr(self.compliance_suggest, 'to_alipay_dict'):
                params['compliance_suggest'] = self.compliance_suggest.to_alipay_dict()
            else:
                params['compliance_suggest'] = self.compliance_suggest
        if self.ocr:
            if hasattr(self.ocr, 'to_alipay_dict'):
                params['ocr'] = self.ocr.to_alipay_dict()
            else:
                params['ocr'] = self.ocr
        if self.ocr_check_suggest:
            if hasattr(self.ocr_check_suggest, 'to_alipay_dict'):
                params['ocr_check_suggest'] = self.ocr_check_suggest.to_alipay_dict()
            else:
                params['ocr_check_suggest'] = self.ocr_check_suggest
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertAuditResult()
        if 'authority_check_retcode' in d:
            o.authority_check_retcode = d['authority_check_retcode']
        if 'authority_check_retmessage' in d:
            o.authority_check_retmessage = d['authority_check_retmessage']
        if 'authority_check_suggest' in d:
            o.authority_check_suggest = d['authority_check_suggest']
        if 'cert_face_suggest' in d:
            o.cert_face_suggest = d['cert_face_suggest']
        if 'compliance_suggest' in d:
            o.compliance_suggest = d['compliance_suggest']
        if 'ocr' in d:
            o.ocr = d['ocr']
        if 'ocr_check_suggest' in d:
            o.ocr_check_suggest = d['ocr_check_suggest']
        return o


