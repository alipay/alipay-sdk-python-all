#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AAAAAtest import AAAAAtest
from alipay.aop.api.domain.AAAAAtest import AAAAAtest


class AlipayOpenOperationOpenbizmockTestdcQueryModel(object):

    def __init__(self):
        self._a = None
        self._a_open_id = None
        self._a_uid = None
        self._aa = None
        self._aaaaa = None
        self._aaaaa_open_id = None
        self._ab = None
        self._ac = None
        self._ad = None
        self._ae = None
        self._b = None
        self._c = None
        self._d = None
        self._data = None
        self._e = None
        self._g = None
        self._i = None
        self._mn = None
        self._open_id = None
        self._sss = None
        self._uid = None
        self._uid_2_open_id = None
        self._uid_open_id = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def a_open_id(self):
        return self._a_open_id

    @a_open_id.setter
    def a_open_id(self, value):
        self._a_open_id = value
    @property
    def a_uid(self):
        return self._a_uid

    @a_uid.setter
    def a_uid(self, value):
        self._a_uid = value
    @property
    def aa(self):
        return self._aa

    @aa.setter
    def aa(self, value):
        if isinstance(value, list):
            self._aa = list()
            for i in value:
                self._aa.append(i)
    @property
    def aaaaa(self):
        return self._aaaaa

    @aaaaa.setter
    def aaaaa(self, value):
        self._aaaaa = value
    @property
    def aaaaa_open_id(self):
        return self._aaaaa_open_id

    @aaaaa_open_id.setter
    def aaaaa_open_id(self, value):
        self._aaaaa_open_id = value
    @property
    def ab(self):
        return self._ab

    @ab.setter
    def ab(self, value):
        self._ab = value
    @property
    def ac(self):
        return self._ac

    @ac.setter
    def ac(self, value):
        self._ac = value
    @property
    def ad(self):
        return self._ad

    @ad.setter
    def ad(self, value):
        self._ad = value
    @property
    def ae(self):
        return self._ae

    @ae.setter
    def ae(self, value):
        self._ae = value
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, value):
        self._e = value
    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        if isinstance(value, AAAAAtest):
            self._g = value
        else:
            self._g = AAAAAtest.from_alipay_dict(value)
    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, value):
        if isinstance(value, list):
            self._i = list()
            for i in value:
                self._i.append(i)
    @property
    def mn(self):
        return self._mn

    @mn.setter
    def mn(self, value):
        if isinstance(value, AAAAAtest):
            self._mn = value
        else:
            self._mn = AAAAAtest.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        self._sss = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_2_open_id(self):
        return self._uid_2_open_id

    @uid_2_open_id.setter
    def uid_2_open_id(self, value):
        self._uid_2_open_id = value
    @property
    def uid_open_id(self):
        return self._uid_open_id

    @uid_open_id.setter
    def uid_open_id(self, value):
        self._uid_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.a:
            if hasattr(self.a, 'to_alipay_dict'):
                params['a'] = self.a.to_alipay_dict()
            else:
                params['a'] = self.a
        if self.a_open_id:
            if hasattr(self.a_open_id, 'to_alipay_dict'):
                params['a_open_id'] = self.a_open_id.to_alipay_dict()
            else:
                params['a_open_id'] = self.a_open_id
        if self.a_uid:
            if hasattr(self.a_uid, 'to_alipay_dict'):
                params['a_uid'] = self.a_uid.to_alipay_dict()
            else:
                params['a_uid'] = self.a_uid
        if self.aa:
            if isinstance(self.aa, list):
                for i in range(0, len(self.aa)):
                    element = self.aa[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.aa[i] = element.to_alipay_dict()
            if hasattr(self.aa, 'to_alipay_dict'):
                params['aa'] = self.aa.to_alipay_dict()
            else:
                params['aa'] = self.aa
        if self.aaaaa:
            if hasattr(self.aaaaa, 'to_alipay_dict'):
                params['aaaaa'] = self.aaaaa.to_alipay_dict()
            else:
                params['aaaaa'] = self.aaaaa
        if self.aaaaa_open_id:
            if hasattr(self.aaaaa_open_id, 'to_alipay_dict'):
                params['aaaaa_open_id'] = self.aaaaa_open_id.to_alipay_dict()
            else:
                params['aaaaa_open_id'] = self.aaaaa_open_id
        if self.ab:
            if hasattr(self.ab, 'to_alipay_dict'):
                params['ab'] = self.ab.to_alipay_dict()
            else:
                params['ab'] = self.ab
        if self.ac:
            if hasattr(self.ac, 'to_alipay_dict'):
                params['ac'] = self.ac.to_alipay_dict()
            else:
                params['ac'] = self.ac
        if self.ad:
            if hasattr(self.ad, 'to_alipay_dict'):
                params['ad'] = self.ad.to_alipay_dict()
            else:
                params['ad'] = self.ad
        if self.ae:
            if hasattr(self.ae, 'to_alipay_dict'):
                params['ae'] = self.ae.to_alipay_dict()
            else:
                params['ae'] = self.ae
        if self.b:
            if hasattr(self.b, 'to_alipay_dict'):
                params['b'] = self.b.to_alipay_dict()
            else:
                params['b'] = self.b
        if self.c:
            if hasattr(self.c, 'to_alipay_dict'):
                params['c'] = self.c.to_alipay_dict()
            else:
                params['c'] = self.c
        if self.d:
            if hasattr(self.d, 'to_alipay_dict'):
                params['d'] = self.d.to_alipay_dict()
            else:
                params['d'] = self.d
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.e:
            if hasattr(self.e, 'to_alipay_dict'):
                params['e'] = self.e.to_alipay_dict()
            else:
                params['e'] = self.e
        if self.g:
            if hasattr(self.g, 'to_alipay_dict'):
                params['g'] = self.g.to_alipay_dict()
            else:
                params['g'] = self.g
        if self.i:
            if isinstance(self.i, list):
                for i in range(0, len(self.i)):
                    element = self.i[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.i[i] = element.to_alipay_dict()
            if hasattr(self.i, 'to_alipay_dict'):
                params['i'] = self.i.to_alipay_dict()
            else:
                params['i'] = self.i
        if self.mn:
            if hasattr(self.mn, 'to_alipay_dict'):
                params['mn'] = self.mn.to_alipay_dict()
            else:
                params['mn'] = self.mn
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.sss:
            if hasattr(self.sss, 'to_alipay_dict'):
                params['sss'] = self.sss.to_alipay_dict()
            else:
                params['sss'] = self.sss
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.uid_2_open_id:
            if hasattr(self.uid_2_open_id, 'to_alipay_dict'):
                params['uid_2_open_id'] = self.uid_2_open_id.to_alipay_dict()
            else:
                params['uid_2_open_id'] = self.uid_2_open_id
        if self.uid_open_id:
            if hasattr(self.uid_open_id, 'to_alipay_dict'):
                params['uid_open_id'] = self.uid_open_id.to_alipay_dict()
            else:
                params['uid_open_id'] = self.uid_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockTestdcQueryModel()
        if 'a' in d:
            o.a = d['a']
        if 'a_open_id' in d:
            o.a_open_id = d['a_open_id']
        if 'a_uid' in d:
            o.a_uid = d['a_uid']
        if 'aa' in d:
            o.aa = d['aa']
        if 'aaaaa' in d:
            o.aaaaa = d['aaaaa']
        if 'aaaaa_open_id' in d:
            o.aaaaa_open_id = d['aaaaa_open_id']
        if 'ab' in d:
            o.ab = d['ab']
        if 'ac' in d:
            o.ac = d['ac']
        if 'ad' in d:
            o.ad = d['ad']
        if 'ae' in d:
            o.ae = d['ae']
        if 'b' in d:
            o.b = d['b']
        if 'c' in d:
            o.c = d['c']
        if 'd' in d:
            o.d = d['d']
        if 'data' in d:
            o.data = d['data']
        if 'e' in d:
            o.e = d['e']
        if 'g' in d:
            o.g = d['g']
        if 'i' in d:
            o.i = d['i']
        if 'mn' in d:
            o.mn = d['mn']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'sss' in d:
            o.sss = d['sss']
        if 'uid' in d:
            o.uid = d['uid']
        if 'uid_2_open_id' in d:
            o.uid_2_open_id = d['uid_2_open_id']
        if 'uid_open_id' in d:
            o.uid_open_id = d['uid_open_id']
        return o


