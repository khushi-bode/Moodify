-- Suggestions Seed Data
-- Covers 8 emotions: Happy, Surprise, Neutral, Contempt, Sad, Fear, Angry, Disgust
-- Covers times of day: morning, afternoon, evening, night, any

INSERT INTO public.suggestions (emotion, time_of_day, base_text) VALUES
-- Happy
('Happy', 'morning', 'Start your day by writing down one thing you are looking forward to.'),
('Happy', 'afternoon', 'Share your positive energy by sending a quick kind message to a friend.'),
('Happy', 'evening', 'Take a moment to reflect on the best part of your day.'),
('Happy', 'any', 'Channel your good mood into a creative activity for 10 minutes.'),

-- Surprise
('Surprise', 'morning', 'Take 3 deep breaths to ground yourself before starting the day.'),
('Surprise', 'afternoon', 'Step away from your screen for a 5-minute walking break.'),
('Surprise', 'evening', 'Write down what caught you off guard today and how you handled it.'),
('Surprise', 'any', 'Drink a glass of water and stretch your arms overhead.'),

-- Neutral
('Neutral', 'morning', 'Set one small, achievable goal for today.'),
('Neutral', 'afternoon', 'Do a quick body scan to see where you might be holding tension.'),
('Neutral', 'evening', 'Listen to a relaxing song while preparing for bed.'),
('Neutral', 'any', 'Take a 5-minute break to look out the window.'),

-- Contempt
('Contempt', 'morning', 'Try a 5-minute guided meditation focused on letting go.'),
('Contempt', 'afternoon', 'Write down one positive thing about a challenging situation.'),
('Contempt', 'evening', 'Disconnect from screens for 30 minutes before bed.'),
('Contempt', 'any', 'Take 5 deep breaths, focusing on relaxing your jaw and shoulders.'),

-- Sad
('Sad', 'morning', 'Make your favorite warm beverage and enjoy it without distractions.'),
('Sad', 'afternoon', 'Reach out to someone you trust just to say hello.'),
('Sad', 'evening', 'Watch or read something comforting and familiar.'),
('Sad', 'any', 'Be gentle with yourself and take a 10-minute rest.'),

-- Fear
('Fear', 'morning', 'Write down your worries, then write one step you can take for each.'),
('Fear', 'afternoon', 'Try the 5-4-3-2-1 grounding technique to center yourself.'),
('Fear', 'evening', 'Do some gentle stretching to release physical tension.'),
('Fear', 'any', 'Focus on your breathing: inhale for 4 seconds, exhale for 6 seconds.'),

-- Angry
('Angry', 'morning', 'Do a quick, high-energy workout to release built-up tension.'),
('Angry', 'afternoon', 'Step outside for a change of scenery and fresh air.'),
('Angry', 'evening', 'Write a letter expressing your frustrations, then throw it away.'),
('Angry', 'any', 'Splash cold water on your face to help reset your nervous system.'),

-- Disgust
('Disgust', 'morning', 'Focus on something beautiful or pleasant in your immediate environment.'),
('Disgust', 'afternoon', 'Declutter one small space on your desk or in your room.'),
('Disgust', 'evening', 'Take a warm, relaxing shower to physically and mentally reset.'),
('Disgust', 'any', 'Engage your senses with a pleasant scent, like a candle or essential oil.');
