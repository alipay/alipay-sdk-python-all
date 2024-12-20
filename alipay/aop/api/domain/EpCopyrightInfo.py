#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpCopyrightInfo(object):

    def __init__(self):
        self._copyright_holder = None
        self._czwcrq = None
        self._flh = None
        self._nationality = None
        self._proclamation_date = None
        self._proclamation_type = None
        self._register_date = None
        self._register_number = None
        self._rjzzqdjh = None
        self._scfbrq = None
        self._serial_number = None
        self._software_abbreviation_name = None
        self._software_full_name = None
        self._software_name = None
        self._version_number = None
        self._work_name = None
        self._zplb = None

    @property
    def copyright_holder(self):
        return self._copyright_holder

    @copyright_holder.setter
    def copyright_holder(self, value):
        self._copyright_holder = value
    @property
    def czwcrq(self):
        return self._czwcrq

    @czwcrq.setter
    def czwcrq(self, value):
        self._czwcrq = value
    @property
    def flh(self):
        return self._flh

    @flh.setter
    def flh(self, value):
        self._flh = value
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value
    @property
    def proclamation_date(self):
        return self._proclamation_date

    @proclamation_date.setter
    def proclamation_date(self, value):
        self._proclamation_date = value
    @property
    def proclamation_type(self):
        return self._proclamation_type

    @proclamation_type.setter
    def proclamation_type(self, value):
        self._proclamation_type = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def register_number(self):
        return self._register_number

    @register_number.setter
    def register_number(self, value):
        self._register_number = value
    @property
    def rjzzqdjh(self):
        return self._rjzzqdjh

    @rjzzqdjh.setter
    def rjzzqdjh(self, value):
        self._rjzzqdjh = value
    @property
    def scfbrq(self):
        return self._scfbrq

    @scfbrq.setter
    def scfbrq(self, value):
        self._scfbrq = value
    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value
    @property
    def software_abbreviation_name(self):
        return self._software_abbreviation_name

    @software_abbreviation_name.setter
    def software_abbreviation_name(self, value):
        self._software_abbreviation_name = value
    @property
    def software_full_name(self):
        return self._software_full_name

    @software_full_name.setter
    def software_full_name(self, value):
        self._software_full_name = value
    @property
    def software_name(self):
        return self._software_name

    @software_name.setter
    def software_name(self, value):
        self._software_name = value
    @property
    def version_number(self):
        return self._version_number

    @version_number.setter
    def version_number(self, value):
        self._version_number = value
    @property
    def work_name(self):
        return self._work_name

    @work_name.setter
    def work_name(self, value):
        self._work_name = value
    @property
    def zplb(self):
        return self._zplb

    @zplb.setter
    def zplb(self, value):
        self._zplb = value


    def to_alipay_dict(self):
        params = dict()
        if self.copyright_holder:
            if hasattr(self.copyright_holder, 'to_alipay_dict'):
                params['copyright_holder'] = self.copyright_holder.to_alipay_dict()
            else:
                params['copyright_holder'] = self.copyright_holder
        if self.czwcrq:
            if hasattr(self.czwcrq, 'to_alipay_dict'):
                params['czwcrq'] = self.czwcrq.to_alipay_dict()
            else:
                params['czwcrq'] = self.czwcrq
        if self.flh:
            if hasattr(self.flh, 'to_alipay_dict'):
                params['flh'] = self.flh.to_alipay_dict()
            else:
                params['flh'] = self.flh
        if self.nationality:
            if hasattr(self.nationality, 'to_alipay_dict'):
                params['nationality'] = self.nationality.to_alipay_dict()
            else:
                params['nationality'] = self.nationality
        if self.proclamation_date:
            if hasattr(self.proclamation_date, 'to_alipay_dict'):
                params['proclamation_date'] = self.proclamation_date.to_alipay_dict()
            else:
                params['proclamation_date'] = self.proclamation_date
        if self.proclamation_type:
            if hasattr(self.proclamation_type, 'to_alipay_dict'):
                params['proclamation_type'] = self.proclamation_type.to_alipay_dict()
            else:
                params['proclamation_type'] = self.proclamation_type
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.register_number:
            if hasattr(self.register_number, 'to_alipay_dict'):
                params['register_number'] = self.register_number.to_alipay_dict()
            else:
                params['register_number'] = self.register_number
        if self.rjzzqdjh:
            if hasattr(self.rjzzqdjh, 'to_alipay_dict'):
                params['rjzzqdjh'] = self.rjzzqdjh.to_alipay_dict()
            else:
                params['rjzzqdjh'] = self.rjzzqdjh
        if self.scfbrq:
            if hasattr(self.scfbrq, 'to_alipay_dict'):
                params['scfbrq'] = self.scfbrq.to_alipay_dict()
            else:
                params['scfbrq'] = self.scfbrq
        if self.serial_number:
            if hasattr(self.serial_number, 'to_alipay_dict'):
                params['serial_number'] = self.serial_number.to_alipay_dict()
            else:
                params['serial_number'] = self.serial_number
        if self.software_abbreviation_name:
            if hasattr(self.software_abbreviation_name, 'to_alipay_dict'):
                params['software_abbreviation_name'] = self.software_abbreviation_name.to_alipay_dict()
            else:
                params['software_abbreviation_name'] = self.software_abbreviation_name
        if self.software_full_name:
            if hasattr(self.software_full_name, 'to_alipay_dict'):
                params['software_full_name'] = self.software_full_name.to_alipay_dict()
            else:
                params['software_full_name'] = self.software_full_name
        if self.software_name:
            if hasattr(self.software_name, 'to_alipay_dict'):
                params['software_name'] = self.software_name.to_alipay_dict()
            else:
                params['software_name'] = self.software_name
        if self.version_number:
            if hasattr(self.version_number, 'to_alipay_dict'):
                params['version_number'] = self.version_number.to_alipay_dict()
            else:
                params['version_number'] = self.version_number
        if self.work_name:
            if hasattr(self.work_name, 'to_alipay_dict'):
                params['work_name'] = self.work_name.to_alipay_dict()
            else:
                params['work_name'] = self.work_name
        if self.zplb:
            if hasattr(self.zplb, 'to_alipay_dict'):
                params['zplb'] = self.zplb.to_alipay_dict()
            else:
                params['zplb'] = self.zplb
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpCopyrightInfo()
        if 'copyright_holder' in d:
            o.copyright_holder = d['copyright_holder']
        if 'czwcrq' in d:
            o.czwcrq = d['czwcrq']
        if 'flh' in d:
            o.flh = d['flh']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'proclamation_date' in d:
            o.proclamation_date = d['proclamation_date']
        if 'proclamation_type' in d:
            o.proclamation_type = d['proclamation_type']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'register_number' in d:
            o.register_number = d['register_number']
        if 'rjzzqdjh' in d:
            o.rjzzqdjh = d['rjzzqdjh']
        if 'scfbrq' in d:
            o.scfbrq = d['scfbrq']
        if 'serial_number' in d:
            o.serial_number = d['serial_number']
        if 'software_abbreviation_name' in d:
            o.software_abbreviation_name = d['software_abbreviation_name']
        if 'software_full_name' in d:
            o.software_full_name = d['software_full_name']
        if 'software_name' in d:
            o.software_name = d['software_name']
        if 'version_number' in d:
            o.version_number = d['version_number']
        if 'work_name' in d:
            o.work_name = d['work_name']
        if 'zplb' in d:
            o.zplb = d['zplb']
        return o


