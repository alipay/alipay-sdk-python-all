#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CaSdnDTO import CaSdnDTO
from alipay.aop.api.domain.CaSdnDTO import CaSdnDTO
from alipay.aop.api.domain.CommonListDTO import CommonListDTO


class PdfCertificateResult(object):

    def __init__(self):
        self._ca_issuer = None
        self._ca_subject = None
        self._failed_reason = None
        self._issuer_dn = None
        self._not_after = None
        self._not_before = None
        self._public_key_format = None
        self._serial_number = None
        self._sign_cert_version = None
        self._sign_date = None
        self._sign_name = None
        self._subject_dn = None
        self._time_stamp_date = None
        self._verified = None
        self._verify_signature = None
        self._verify_timestamp_imprint = None

    @property
    def ca_issuer(self):
        return self._ca_issuer

    @ca_issuer.setter
    def ca_issuer(self, value):
        if isinstance(value, CaSdnDTO):
            self._ca_issuer = value
        else:
            self._ca_issuer = CaSdnDTO.from_alipay_dict(value)
    @property
    def ca_subject(self):
        return self._ca_subject

    @ca_subject.setter
    def ca_subject(self, value):
        if isinstance(value, CaSdnDTO):
            self._ca_subject = value
        else:
            self._ca_subject = CaSdnDTO.from_alipay_dict(value)
    @property
    def failed_reason(self):
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, value):
        if isinstance(value, list):
            self._failed_reason = list()
            for i in value:
                if isinstance(i, CommonListDTO):
                    self._failed_reason.append(i)
                else:
                    self._failed_reason.append(CommonListDTO.from_alipay_dict(i))
    @property
    def issuer_dn(self):
        return self._issuer_dn

    @issuer_dn.setter
    def issuer_dn(self, value):
        self._issuer_dn = value
    @property
    def not_after(self):
        return self._not_after

    @not_after.setter
    def not_after(self, value):
        self._not_after = value
    @property
    def not_before(self):
        return self._not_before

    @not_before.setter
    def not_before(self, value):
        self._not_before = value
    @property
    def public_key_format(self):
        return self._public_key_format

    @public_key_format.setter
    def public_key_format(self, value):
        self._public_key_format = value
    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value
    @property
    def sign_cert_version(self):
        return self._sign_cert_version

    @sign_cert_version.setter
    def sign_cert_version(self, value):
        self._sign_cert_version = value
    @property
    def sign_date(self):
        return self._sign_date

    @sign_date.setter
    def sign_date(self, value):
        self._sign_date = value
    @property
    def sign_name(self):
        return self._sign_name

    @sign_name.setter
    def sign_name(self, value):
        self._sign_name = value
    @property
    def subject_dn(self):
        return self._subject_dn

    @subject_dn.setter
    def subject_dn(self, value):
        self._subject_dn = value
    @property
    def time_stamp_date(self):
        return self._time_stamp_date

    @time_stamp_date.setter
    def time_stamp_date(self, value):
        self._time_stamp_date = value
    @property
    def verified(self):
        return self._verified

    @verified.setter
    def verified(self, value):
        self._verified = value
    @property
    def verify_signature(self):
        return self._verify_signature

    @verify_signature.setter
    def verify_signature(self, value):
        self._verify_signature = value
    @property
    def verify_timestamp_imprint(self):
        return self._verify_timestamp_imprint

    @verify_timestamp_imprint.setter
    def verify_timestamp_imprint(self, value):
        self._verify_timestamp_imprint = value


    def to_alipay_dict(self):
        params = dict()
        if self.ca_issuer:
            if hasattr(self.ca_issuer, 'to_alipay_dict'):
                params['ca_issuer'] = self.ca_issuer.to_alipay_dict()
            else:
                params['ca_issuer'] = self.ca_issuer
        if self.ca_subject:
            if hasattr(self.ca_subject, 'to_alipay_dict'):
                params['ca_subject'] = self.ca_subject.to_alipay_dict()
            else:
                params['ca_subject'] = self.ca_subject
        if self.failed_reason:
            if isinstance(self.failed_reason, list):
                for i in range(0, len(self.failed_reason)):
                    element = self.failed_reason[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.failed_reason[i] = element.to_alipay_dict()
            if hasattr(self.failed_reason, 'to_alipay_dict'):
                params['failed_reason'] = self.failed_reason.to_alipay_dict()
            else:
                params['failed_reason'] = self.failed_reason
        if self.issuer_dn:
            if hasattr(self.issuer_dn, 'to_alipay_dict'):
                params['issuer_dn'] = self.issuer_dn.to_alipay_dict()
            else:
                params['issuer_dn'] = self.issuer_dn
        if self.not_after:
            if hasattr(self.not_after, 'to_alipay_dict'):
                params['not_after'] = self.not_after.to_alipay_dict()
            else:
                params['not_after'] = self.not_after
        if self.not_before:
            if hasattr(self.not_before, 'to_alipay_dict'):
                params['not_before'] = self.not_before.to_alipay_dict()
            else:
                params['not_before'] = self.not_before
        if self.public_key_format:
            if hasattr(self.public_key_format, 'to_alipay_dict'):
                params['public_key_format'] = self.public_key_format.to_alipay_dict()
            else:
                params['public_key_format'] = self.public_key_format
        if self.serial_number:
            if hasattr(self.serial_number, 'to_alipay_dict'):
                params['serial_number'] = self.serial_number.to_alipay_dict()
            else:
                params['serial_number'] = self.serial_number
        if self.sign_cert_version:
            if hasattr(self.sign_cert_version, 'to_alipay_dict'):
                params['sign_cert_version'] = self.sign_cert_version.to_alipay_dict()
            else:
                params['sign_cert_version'] = self.sign_cert_version
        if self.sign_date:
            if hasattr(self.sign_date, 'to_alipay_dict'):
                params['sign_date'] = self.sign_date.to_alipay_dict()
            else:
                params['sign_date'] = self.sign_date
        if self.sign_name:
            if hasattr(self.sign_name, 'to_alipay_dict'):
                params['sign_name'] = self.sign_name.to_alipay_dict()
            else:
                params['sign_name'] = self.sign_name
        if self.subject_dn:
            if hasattr(self.subject_dn, 'to_alipay_dict'):
                params['subject_dn'] = self.subject_dn.to_alipay_dict()
            else:
                params['subject_dn'] = self.subject_dn
        if self.time_stamp_date:
            if hasattr(self.time_stamp_date, 'to_alipay_dict'):
                params['time_stamp_date'] = self.time_stamp_date.to_alipay_dict()
            else:
                params['time_stamp_date'] = self.time_stamp_date
        if self.verified:
            if hasattr(self.verified, 'to_alipay_dict'):
                params['verified'] = self.verified.to_alipay_dict()
            else:
                params['verified'] = self.verified
        if self.verify_signature:
            if hasattr(self.verify_signature, 'to_alipay_dict'):
                params['verify_signature'] = self.verify_signature.to_alipay_dict()
            else:
                params['verify_signature'] = self.verify_signature
        if self.verify_timestamp_imprint:
            if hasattr(self.verify_timestamp_imprint, 'to_alipay_dict'):
                params['verify_timestamp_imprint'] = self.verify_timestamp_imprint.to_alipay_dict()
            else:
                params['verify_timestamp_imprint'] = self.verify_timestamp_imprint
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PdfCertificateResult()
        if 'ca_issuer' in d:
            o.ca_issuer = d['ca_issuer']
        if 'ca_subject' in d:
            o.ca_subject = d['ca_subject']
        if 'failed_reason' in d:
            o.failed_reason = d['failed_reason']
        if 'issuer_dn' in d:
            o.issuer_dn = d['issuer_dn']
        if 'not_after' in d:
            o.not_after = d['not_after']
        if 'not_before' in d:
            o.not_before = d['not_before']
        if 'public_key_format' in d:
            o.public_key_format = d['public_key_format']
        if 'serial_number' in d:
            o.serial_number = d['serial_number']
        if 'sign_cert_version' in d:
            o.sign_cert_version = d['sign_cert_version']
        if 'sign_date' in d:
            o.sign_date = d['sign_date']
        if 'sign_name' in d:
            o.sign_name = d['sign_name']
        if 'subject_dn' in d:
            o.subject_dn = d['subject_dn']
        if 'time_stamp_date' in d:
            o.time_stamp_date = d['time_stamp_date']
        if 'verified' in d:
            o.verified = d['verified']
        if 'verify_signature' in d:
            o.verify_signature = d['verify_signature']
        if 'verify_timestamp_imprint' in d:
            o.verify_timestamp_imprint = d['verify_timestamp_imprint']
        return o


