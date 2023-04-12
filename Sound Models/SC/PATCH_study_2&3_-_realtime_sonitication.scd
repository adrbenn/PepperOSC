//Claudio Panariello
//
// claudiop[at]kth[dot]se
//
//
// PEPPER TEKNISKA PATCH
// with hand position
// Sound specs
s.options.memSize = 2.pow(19); // <<<---------
s.options.blockSize = 256;
{Out.ar(0, SinOsc.ar(440, 0, 0.1))}.play


~pepper = NetAddr.new("127.0.0.1", 3002); //local port to receive from pepper

// Just to check if data are incoming. Leave COMMENTED these lines
OSCFunc({|msg| msg.postln}, '/pepperdata', recvPort:3002);
// OSCFunc({|msg| msg.postln}, '/pepperdata', recvPort:3002);
// OSCFunc({|msg| msg.postln}, '/pepperdata', recvPort:3002);

(
/*
███████╗██╗   ██╗███╗   ██╗████████╗██╗  ██╗███████╗
██╔════╝╚██╗ ██╔╝████╗  ██║╚══██╔══╝██║  ██║██╔════╝
███████╗ ╚████╔╝ ██╔██╗ ██║   ██║   ███████║███████╗
╚════██║  ╚██╔╝  ██║╚██╗██║   ██║   ██╔══██║╚════██║
███████║   ██║   ██║ ╚████║   ██║   ██║  ██║███████║
╚══════╝   ╚═╝   ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
*/
/*
╔═╗┌─┐┬ ┬┌┬┐┌─┐┌─┐┌┬┐┬ ┬
╚═╗├─┤│││ │ │ ││ │ │ ├─┤
╚═╝┴ ┴└┴┘ ┴ └─┘└─┘ ┴ ┴ ┴
*/
~busrev = Bus.audio(s, 2);
SynthDef(\saw, {
	arg which = 0, freq1 = 440, freq2 = 440, freq3 = 440, lagVal = 0.1, cutoff = 15e3, att, sus = 1, rel = 1, curve = \welch, gate = 1, amp1 = 0, amp2 = 0, amp3 = 0, activity = 24;
	var saw = LPF.ar(Saw.ar(freq1.lag3(lagVal)+freq2.lag3(lagVal)+freq3.lag3(lagVal)), cutoff.lag3(lagVal)),
	env = EnvGen.kr(Env.asr(att, sus, rel, curve:curve), gate),
	grainTrig = Impulse.kr(activity.lag3(lagVal)),
	grain = GrainIn.ar(2, grainTrig, 0.05, saw),
	output = Select.ar(which, [saw, grain]), //by default the output is NOT granularised
	amplitude = Slope.kr(amp1.lag3(lagVal)).abs.lag3(0.4);
	//amplitude.poll;

	Out.ar(~busrev, Pan2.ar(output*env, 0, amplitude*0.4));
}).add;

/*
┌─┐┌─┐┌─┐┌┬┐┌┐ ┌─┐┌─┐┬┌─
├┤ ├┤ ├┤  ││├┴┐├─┤│  ├┴┐
└  └─┘└─┘─┴┘└─┘┴ ┴└─┘┴ ┴
*/
~busenv = Bus.audio(s, 1);
SynthDef(\impulse, {arg rel = 0.01, level = 1;
	var
	imp = LFPulse.ar(5000),
	env = EnvGen.kr(Env.perc(0, rel), 1, level, doneAction: 2);
	Out.ar(~busenv, imp*env);
}).add;

SynthDef(\f_synth, {arg fb = 1.07, lag = 0.5, windowsize, wipe = 0.1, freq = 1, rInf1, rInf2, rInf3, level = 1, lagVal = 0.1, gate = 1, rInf = 200, rSup = 200, amp1 = 1, detune = 1;
	var in, feedback, out, output1, chain, out2, rms, control, envfol_in, pan, amplitude, env;
	feedback = LocalIn.ar(1)*fb;
	in = In.ar(~busenv, 1);
	out = LeakDC.ar(feedback + in);
	output1 = BPF.ar(out, LFNoise2.ar(freq, 1, detune.lag3.(lagVal)).range(rInf.lag3(lagVal), rSup.lag3(lagVal)), 0.9, 1);
	amplitude = Slope.kr(level.lag3(lagVal)).abs.lag3(0.4);

	chain = FFT(LocalBuf(windowsize, 1), output1);
	chain = PV_BinScramble(chain, wipe, 1);
	output1 = IFFT(chain);
	LocalOut.ar(output1);
	out2 = FreeVerb.ar(output1);
	rms = RunningSum.rms(Amplitude.ar(out2)).clip(0, 1);
	control = 1.01-(rms.lag2(lag));
	envfol_in = Lag3.ar(rms, lag);
	env = EnvGen.kr(Env.asr(0.1, 1, 1, curve:-4), gate, doneAction:2);
	pan = Pan2.ar(Limiter.ar(output1*control*env), 0, amplitude);
	//pan = Pan2.ar(Limiter.ar(output1*control*env), 0, level.lag3(lagVal));


	Out.ar(~busrev, pan);
}).add;
)




/*
███████╗ ██████╗ ███╗   ██╗██╗███████╗██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗████╗  ██║██║██╔════╝██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗██║   ██║██╔██╗ ██║██║█████╗  ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██║   ██║██║╚██╗██║██║██╔══╝  ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
███████║╚██████╔╝██║ ╚████║██║██║     ██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
*/
(
// reverb
r = Synth(\rev, [\mix, 0.5, \gate, 0]);

// variables for turning on the sound models
~simpleSynthesis = 0;
~subSynthesis = 0;
~feedSynthesis = 0;

//~numSynthsSimple = 1;
~numSynthsSub = 10;
~numSynthsFeed = 2;

~synthsSimple = 0;
~synthSaw = Synth(\saw, [\freq1, 200, \freq2, 1, \freq3, 1, \att, 0.1, \amp1, 0.3, \amp2, 0.3, \activity, 12, \cutoff, 10000, \gate, 0]);

~aux1 = 0; ~aux2 = 0; ~auxE1 = 0; ~auxE2 = 0; ~vector = [0, 0]; ~vectorElbow = [0, 0]; ~af1 = 0; ~af2 = 0; ~auxfE1 = 0; ~auxfE2 = 0; ~vectorF = [0, 0]; ~vectorFElbow = [0, 0];
~rsp = 0; ~rsr  = 0; ~rer = 0;

~synthsSub = Array.fill(~numSynthsSub, 0);
~amps1 = Array.fill(~numSynthsSub, {|i| i}).linexp(0, ~numSynthsSub, 40.0, 0.1);
~amps2 = ~amps1.reverse;
//~bands1 = [1.7, -0.02].interpolate((~numSynthsSub+1)/2, loop:false);
//~bands2 = [-1, -0.11].interpolate((~numSynthsSub+1)/2, loop:false);
//~bands3 = [0.1, 1.6].interpolate((~numSynthsSub+1)/2, loop:false);
~bands1= Array.interpolation(11, 1.7, -0.02);
~bands2= Array.interpolation(11, -1, -0.11);
~bands3= Array.interpolation(11, 0.1, 1.6);

//~numSynthsSub.do({|i| ~synthsSub[i] = Synth(\subtract, [\cFreq, 200*(i+1), \rq, 0.001, \t, 1, \gate, 0, \lagVal, 0.1, \amp1, 0.001]); });

~af1 = 0; ~af2 = 0; ~vectorF = [0, 0];
~synthsFeed = Array.fill(~numSynthsFeed, 0);
~amps1F = Array.fill(~numSynthsFeed, {|i| i}).linexp(0, ~numSynthsFeed, 1.0, 0.01);
~amps2F = ~amps1F.reverse;

OSCFunc({|msg|
	if(msg[1].value == 2, {
		~simpleSynthesis = 1;
		("Soundstart: simple synthesis").postln;
		r.set(\gate, 1);
		~synthSaw.set(\gate, 1);
	}; );

	if(msg[1].value == 1, {
		//~subSynthesis = 1;
		("Soundstart: NO Sound").postln;
		//r.set(\gate, 1);
	}; );

	if(msg[1].value == 3, {
		~feedSynthesis = 1;
		("Soundstart: feedbacks").postln;
		r.set(\gate, 1);
		~numSynthsFeed.do({|i| ~synthsFeed[i] = Synth(\f_synth, [\fb, 1.11, \windowsize, 1024, \wipe, 0.01, \freq, 1, \rInf, 300, \rSup, 500, \level, 0.01, \gate, 1]);});
		Synth(\impulse, [\level, 0.1]);
	}; );
}, '/soundstart', recvPort:3002);


OSCFunc({|msg|
	if((msg[1].asString == "/RShoulderPitch"), {~rsp = 1-msg[3].value.abs});
	if((msg[1].asString == "/RShoulderRoll"), {~rsr = msg[3].value});
	if((msg[1].asString == "/RElbowRoll"), {~rer = msg[3].value});
	~handPos = sqrt((~rsp**2*0.7)+(~rsr**2*1.3))-(~rer/2);
	//("Hand position: "++~handPos).postln;
}, '/pepperdata', recvPort:3002);

/*
╔═╗┌─┐┬ ┬┌┬┐┌─┐┌─┐┌┬┐┬ ┬
╚═╗├─┤│││ │ │ ││ │ │ ├─┤
╚═╝┴ ┴└┴┘ ┴ └─┘└─┘ ┴ ┴ ┴
*/
OSCFunc({|msg|
	if((~simpleSynthesis == 1), {
		//("RShoulderPitch: "++msg[3]).postln;
		~synthSaw.set(\freq1, ~handPos.linexp(0, 1.5, 300, 800));
		~synthSaw.set(\amp1, ~handPos.linlin(0, 1.5, 0, 0.5));
		~synthSaw.set(\cutoff, ~handPos.linlin(0, 1.5, 1000, 11000));
	});
}, '/pepperdata', recvPort:3002);

/*
┌─┐┌─┐┌─┐┌┬┐┌┐ ┌─┐┌─┐┬┌─
├┤ ├┤ ├┤  ││├┴┐├─┤│  ├┴┐
└  └─┘└─┘─┴┘└─┘┴ ┴└─┘┴ ┴
*/
OSCFunc({|msg|
	if((~feedSynthesis == 1), {
		~af2 = ~handPos;
		//~vectorF = [~af1, ~af2].interpolate(2.5, loop:false);
		~vectorF = Array.interpolation(5, ~af1, ~af2);
		{5.do({|n|
			//("Value: "++~vectorF[n].linexp(0, 1.5, 300, 2000)).postln;
			~numSynthsFeed.do({|i|
				~synthsFeed[i].set(
					\rInf, ~vectorF[n].linexp(0, 1.5, 300, 2000),
					\rSup, ~vectorF[n].linexp(0, 1.5, 500, 2500),
					\level, ~vectorF[n].linexp(0, 1.5, 0.007, 0.32)
					//\rInf, ~vectorF[n].linexp(-0.02, 1.8, 1000, 300),
					//\rSup, ~vectorF[n].linexp(-0.02, 1.8, 1200, 500),
					//\level, ~vectorF[n].linexp(-0.02, 1.8, 0.3, 0.01)
					//\amp1, ~vectorF[n].linexp(-0.02, 1.8, ~amps2F[i], ~amps1F[i])
				);
			});
			0.01.wait;}) }.fork;
		~af1 = ~af2;
	});

}, '/pepperdata', recvPort:3002);

OSCFunc({|msg| if(msg[1].value == 0, {
	("Soundstop: "++msg[1]).postln;
	r.set(\gate, 0);
	if(~simpleSynthesis == 1,{~synthSaw.set(\gate, 0); ~simpleSynthesis = 0; });
	//if(~subSynthesis == 1,{~numSynthsSub.do({|i| ~synthsSub[i].set(\gate, 0)}); ~subSynthesis = 0; });
	if(~feedSynthesis == 1,{~numSynthsFeed.do({|i| ~synthsFeed[i].set(\gate, 0)}); ~feedSynthesis = 0; });
};);
}, '/soundstop', recvPort:3002);

)

// EOF //